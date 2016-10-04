from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import BlogPost


class BlogPostAdmin(TranslatableAdmin):

  list_display = ['pk', 'get_title', 'date', 'published']

  def get_title(self, obj):
        return obj.title

admin.site.register(BlogPost, BlogPostAdmin)
