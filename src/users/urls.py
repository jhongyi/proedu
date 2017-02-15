from django.conf.urls import url

from .views import (
    UserListAPIView,
    UserCreateListAPIView,
    UserUpdateListAPIView,
)

urlpatterns = [
    url(r'^list/$', UserListAPIView.as_view(), name='get_users'),
    url(r'^create/$', UserCreateListAPIView.as_view(), name='create_user'),
    url(r'^update/(?P<pk>[0-9]+)/$', UserUpdateListAPIView.as_view(), name='update_user'),
]