from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from hvad.models import TranslatableModel, TranslatedFields

# Create your models here.
class BlogPost(TranslatableModel):
    header_image = models.ImageField(null=True, blank=True)
    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        body = models.TextField(null=True, blank=True)
    )

    def __unicode__(self):
        return self.title
