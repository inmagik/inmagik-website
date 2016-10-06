from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django_s3_storage.storage import S3Storage
from django.utils.html import mark_safe

from PIL import Image
import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.
class NamedFile(models.Model):
    name = models.CharField(max_length=300)
    upload = models.FileField(null=True, blank=True,
        upload_to="cmz-files",
        storage=S3Storage())

    thumb = models.FileField(
        null=True, blank=True, editable=False,
        upload_to="cmz-files",
        storage=S3Storage()
    )

    def thumb_preview(self):
        if self.thumb:
            return mark_safe('<img src="%s" width="100" height="auto" />' % (self.thumb.url))
        return ""

    thumb_preview.short_description = 'Thumb'


    def save(self, *args, **kwargs):
        self.thumb.delete(False)
        try:
            im = Image.open(self.upload.file)
            size = (100, 100*im.size[0]/im.size[1])
            im.thumbnail(size, Image.ANTIALIAS)
            thumb_io = StringIO.StringIO()
            im.save(thumb_io, format='JPEG')
            # Create a new Django file-like object to be used in models as ImageField using
            # InMemoryUploadedFile.  If you look at the source in Django, a
            # SimpleUploadedFile is essentially instantiated similarly to what is shown here
            thumb_file = InMemoryUploadedFile(thumb_io, None, '%s.thumb.jpg' % self.upload.name,
                'image/jpeg', thumb_io.len, None)
            self.thumb = thumb_file
        except:
            pass

        return super(NamedFile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=NamedFile)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.upload.delete(False)
    instance.thumb.delete(False)
