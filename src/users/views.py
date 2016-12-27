from django.contrib.auth.models import User
from users.serializers import UserSerializer
from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView
)

class UserListAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
