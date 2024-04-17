from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import (
    ProductSerializer,
    CategorySerializer
)

from apps.product.models import (
    ProductProxy,
    Product,
    Category
)


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductProxy.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(
        method="get",
        operation_description="Получение списка товаров",
        operation_summary="Список товаров",
        operation_id="list_products",
        tags=["Products"],
        responses={
            200: openapi.Response(description="OK - Список успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["get"])
    def list_products(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class CategoryModelViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    @swagger_auto_schema(
        method="get",
        operation_description="Получение списка категориев",
        operation_summary="Категории товаров",
        operation_id="Category_products",
        tags=["Category"],
        responses={
            200: openapi.Response(description="OK - Список успешно получен"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Ресурс не найден"),
        },
    )
    @action(detail=True, methods=["get"])
    def list_category(self, request, pk=None):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



