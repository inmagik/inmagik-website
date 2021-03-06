from .models import PortfolioItem
from django_rest_admin.register import rest_admin, RestAdminConfig
from hvad.contrib.restframework import TranslatableModelSerializer
from rest_framework.viewsets import ModelViewSet
from django.utils import translation
from rest_framework.parsers import FileUploadParser, MultiPartParser, JSONParser

class PortfolioItemViewSet(ModelViewSet):
    parser_classes = ( MultiPartParser, JSONParser )
    def get_queryset(self):
        return PortfolioItem.objects.language(translation.get_language()).all()

class PortfolioItemConfig(RestAdminConfig):
    serializer_class = TranslatableModelSerializer
    viewset_class = PortfolioItemViewSet


rest_admin.register(PortfolioItem, PortfolioItemConfig)
