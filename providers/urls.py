from django.conf.urls import url
from providers.views import ProviderList, ProviderDetail


urlpatterns = [
    url(r'^$', ProviderList.as_view(), name='provider-list'),
    url(r'^(?P<pk>\d+)/$', ProviderDetail.as_view(), name='provider-detail'),
]
