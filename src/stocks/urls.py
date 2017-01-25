from django.conf.urls import url

from .views import (
    StockListAPIView,
    StockCreateAPIView,
    StockUpdateAPIView,
    StockDeleteAPIView,
)

urlpatterns = [
    url(r'^list/$', StockListAPIView.as_view(), name='get_stocks'),
    url(r'^create/$', StockCreateAPIView.as_view(), name='create_stocks'),
    url(r'^update/(?P<pk>[0-9]+)/$', StockUpdateAPIView.as_view(), name='update_stocks'),
    url(r'^delete/(?P<pk>[0-9]+)/$', StockDeleteAPIView.as_view(), name='delete_stocks')
]