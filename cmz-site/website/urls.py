from django.conf.urls import url, include
from django.contrib import admin


#patterns = [
    #url(r'', include('cms_core.urls')),
#]

print 123, "xxx"
urlpatterns = [
    url('rest_admin/', include('cmz_jwt_auth.urls'))
]
