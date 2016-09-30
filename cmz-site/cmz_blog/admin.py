from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import BlogPost

admin.site.register(BlogPost, TranslatableAdmin)
