from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from hvad.models import TranslatableModel, TranslatedFields
from django_s3_storage.storage import S3Storage
import markdown

from cmz_files.helpers import replace_cmz_files

# Create your models here.
class BlogPost(TranslatableModel):
    #todo: this should be named "slug" and be translated...
    id = models.CharField(max_length=255, primary_key=True)
    header_image = models.ImageField(null=True, blank=True,
        upload_to="blog-images",
        storage=S3Storage())
    author = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False)


    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        intro = models.TextField(max_length=1000, null=True, blank=True),
        body = models.TextField(null=True, blank=True)
    )

    def html_body(self):
        return markdown.markdown(replace_cmz_files(self.body))

    def html_intro(self):
        return markdown.markdown(self.intro)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']


# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=BlogPost)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.header_image.delete(False)
