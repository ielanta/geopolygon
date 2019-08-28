from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^providers/', include('providers.urls')),
    url(r'^services/', include('service_areas.urls')),
]
