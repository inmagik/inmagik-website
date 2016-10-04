from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from hvad.models import TranslatableModel, TranslatedFields
from hvad.utils import get_translation_aware_manager

from django_s3_storage.storage import S3Storage

# Create your models here.
class Tech(TranslatableModel):

    icon = models.ImageField(null=True, blank=True, upload_to="technology-icons",
        storage=S3Storage()
    )
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        description = models.TextField(null=True, blank=True)
    )

    order = models.IntegerField(blank=True, default=0)

    class Meta:
        ordering = ['order']
        

    def __unicode__(self):
        return self.title
