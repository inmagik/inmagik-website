from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from hvad.models import TranslatableModel, TranslatedFields
from django_s3_storage.storage import S3Storage
import markdown

# Create your models here.
class PortfolioItem(TranslatableModel):
    header_image = models.ImageField(null=True, blank=True,
        upload_to="portfolio-images",
        storage=S3Storage())
    author = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    blue_tags = models.CharField(max_length=200, null=True, blank=True)
    red_tags = models.CharField(max_length=200, null=True, blank=True)

    translations = TranslatedFields(
        title = models.CharField(max_length=255),
        intro = models.TextField(max_length=1000, null=True, blank=True),
        body = models.TextField(null=True, blank=True)
    )

    def html_body(self):
        return markdown.markdown(self.body)

    def html_intro(self):
        return markdown.markdown(self.intro)

    def blue_tags_list(self):
        return self.blue_tags.split(",")

    def red_tags_list(self):
        return self.red_tags.split(",")

    def __unicode__(self):
        return self.title
