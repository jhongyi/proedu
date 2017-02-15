from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_503_SERVICE_UNAVAILABLE,
    HTTP_500_INTERNAL_SERVER_ERROR
)
from rest_framework.views import (
    APIView,
)

from rest_framework.generics import (
    CreateAPIView,
    UpdateAPIView,
)

from rest_framework.permissions import (
    IsAuthenticated,
)

#from django.contrib.auth import authenticate
#from rest_framework.authtoken.models import Token

class UserListAPIView(APIView):

    def post(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class UserCreateListAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        users = self.queryset
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=HTTP_201_CREATED)

class UserUpdateListAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.data, status=HTTP_500_INTERNAL_SERVER_ERROR)
        