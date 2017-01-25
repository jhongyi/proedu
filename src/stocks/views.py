from stocks.models import Stock
from .serializers import StockSerializer
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
    DestroyAPIView,
)

class StockListAPIView(APIView):
    def post(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class StockCreateAPIView(CreateAPIView):
    serializer_class = StockSerializer
    
    def get_queryset(self):
        queryset = Stock.objects.all()
        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

class StockUpdateAPIView(UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.data, status=HTTP_500_INTERNAL_SERVER_ERROR)

class StockDeleteAPIView(DestroyAPIView):
    queryset = Stock.objects.all()
    def list(self, request):
        stocks = Stock.objects.delete(request.data)
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data, status=HTTP_201_CREATED)