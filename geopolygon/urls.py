from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls

API_TITLE = 'GeoPolygon API doc'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^providers/', include('providers.urls')),
    url(r'^services/', include('service_areas.urls')),
    url(r'^docs/', include_docs_urls(title=API_TITLE))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
