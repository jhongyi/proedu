from rest_framework.serializers import (
    CharField,
    EmailField,
    DateTimeField,
    Serializer,
    ModelSerializer,
)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
