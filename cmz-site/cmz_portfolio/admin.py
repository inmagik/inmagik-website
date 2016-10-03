from django.contrib import admin
from hvad.admin import TranslatableAdmin
from .models import PortfolioItem

admin.site.register(PortfolioItem, TranslatableAdmin)

# Register your models here.
