from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import SiteCheckup
from cms_core.views import CMZTemplateMixin

class CreateSiteCheckup(CMZTemplateMixin, CreateView):
    template="site_checkup.html"
    model = SiteCheckup
    fields = ['url']
