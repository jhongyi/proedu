from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_503_SERVICE_UNAVAILABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.generics import (
    CreateAPIView
)

class UserListAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(HTTP_201_CREATED, serializer.data)
