from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from drf_yasg import openapi

from .serializers import (
    OrderSerializer,
    ShippingAddressSerializer,
    OrderItemSerializer
)

from apps.payment.models import (
    ShippingAddress,
    Order,
    OrderItem
)


class ShippingAddressViewSet(viewsets.ModelViewSet):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

    def get_queryset(self):
        try:
            shipping_address = ShippingAddress.objects.get(user=self.request.user)
        except ShippingAddress.DoesNotExist:
            shipping_address = None
        return shipping_address




'''
@login_required(login_url='account:login')
def shipping(request):
    pass

def checkout(reqeust):
    pass

def complete_order(reqeust):
    pass

def pyament_success(reqeust):
    pass

def payment_failed(reqeust):
    pass

def admin_order_pdf(request, order_id):
    pass





'''




















'''
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
    def products_list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        # queryset = self.queryset.get(slug=kwargs.get("slug"))
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        method="get",
        operation_description="Получение детальной информации о товаре",
        operation_summary="Детальная информация о товаре",
        operation_id="product_detail",
        tags=["Products"],
        responses={
            200: openapi.Response(description="OK - Детальная информация о продукте успешно получена"),
            400: openapi.Response(description="Bad Request - Неверный запрос"),
            401: openapi.Response(description="Unauthorized - Неавторизованный запрос"),
            404: openapi.Response(description="Not Found - Продукт не найден"),
        },
    )
    @action(detail=True, methods=["get"])
    def product_detail(self, request, *args, **kwargs):
        try:
            # product = self.get_object()
            product = self.queryset.get(slug=kwargs.get("slug"))
        except ProductProxy.DoesNotExist:
            return Response(
                {
                    "detail": "Продукт не найден."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.get_serializer(product)
        return Response(serializer.data)

'''
