from .models import Tech
from django_rest_admin.register import rest_admin, RestAdminConfig
from hvad.contrib.restframework import TranslatableModelSerializer
from rest_framework.viewsets import ModelViewSet
from django.utils import translation

class TechViewSet(ModelViewSet):
    def get_queryset(self):
        return Tech.objects.language(translation.get_language()).all()

class TechConfig(RestAdminConfig):
    serializer_class = TranslatableModelSerializer
    viewset_class = TechViewSet


rest_admin.register(Tech, TechConfig)
