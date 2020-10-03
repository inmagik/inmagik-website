from __future__ import unicode_literals

from django.db import models

class SiteCheckup(models.Model):
    url = models.URLField()
