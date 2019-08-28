from django.conf.urls import url
from service_areas.views import ServiceAreaList, ServiceAreaDetail, ServiceAreaPoint


urlpatterns = [
    url(r'^$', ServiceAreaList.as_view(), name='service-area-list'),
    url(r'^(?P<pk>\d+)/$', ServiceAreaDetail.as_view(), name='service-area-detail'),
    url(r'^point/$', ServiceAreaPoint.as_view(), name='service-area-list'),
]
