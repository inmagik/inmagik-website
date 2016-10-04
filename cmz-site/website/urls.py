from django.conf.urls import url, include
from django.contrib import admin


#patterns = [
    #url(r'', include('cms_core.urls')),
#]

urlpatterns = [
    url('api/', include('cmz_jwt_auth.urls'))
]
