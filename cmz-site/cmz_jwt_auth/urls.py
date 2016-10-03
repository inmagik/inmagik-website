from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import MeView

urlpatterns = [
    url(r'^me/', MeView.as_view()),
    url(r'^auth/', obtain_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token)
]
