from django.conf.urls import url

from .views import (
    StockListAPIView,
)

urlpatterns = [
    url(r'^create/$', StockListAPIView.as_view(), name='stocks'),
]