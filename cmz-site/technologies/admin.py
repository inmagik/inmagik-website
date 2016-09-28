from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import Tech

admin.site.register(Tech, TranslatableAdmin)
