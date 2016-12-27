from django.conf.urls import url

from .views import (
    UserListAPIView,
)

urlpatterns = [
    url(r'^create/$', UserListAPIView.as_view(), name='users'),
]
