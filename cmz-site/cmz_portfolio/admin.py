from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import PortfolioItem

class PortfolioItemAdmin(TranslatableAdmin):

  list_display = ['pk', 'get_title', 'order', 'published']

  def get_title(self, obj):
        return obj.title

admin.site.register(PortfolioItem, PortfolioItemAdmin)
