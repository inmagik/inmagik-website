from django.contrib import admin
from .models import NamedFile

class NamedFileAdmin(admin.ModelAdmin):
    readonly_fields = ['thumb']
    list_display = ["name", "thumb_preview"]

admin.site.register(NamedFile, NamedFileAdmin)
