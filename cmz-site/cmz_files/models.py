from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django_s3_storage.storage import S3Storage

# Create your models here.
class NamedFile(models.Model):
    name = models.CharField(max_length=300)
    upload = models.ImageField(null=True, blank=True,
        upload_to="cmz-files",
        storage=S3Storage())

    def __unicode__(self):
        return self.name



# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

@receiver(pre_delete, sender=NamedFile)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.upload.delete(False)
