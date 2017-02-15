from django.contrib.auth.models import User
#from rest_framework.serializers import (
#    ModelSerializer,
#)

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    # change field name -> use source
    user_id = serializers.ReadOnlyField(source='id')
    
    class Meta:
        model = User
        fields = ('user_id', 'email', 'username', 'first_name', 'last_name' , 'password', 'is_active', 'is_staff')
        #read_only_fields = ('id',)
        #exclude = ('id', 'last_login', 'is_superuser', 'date_joined', 'groups', 'user_permissions')
        extra_kwargs = {
            'password': {'write_only': True}
        }
