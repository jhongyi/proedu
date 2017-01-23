from stocks.models import Stock
from rest_framework.serializers import (
    CharField,
    EmailField,
    DateTimeField,
    Serializer,
    ModelSerializer,
)

class StockSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
