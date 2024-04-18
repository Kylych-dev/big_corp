from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from drf_yasg import openapi

from .serializers import (
    CartSerializer,
)

from apps.product.models import (
    ProductProxy,
    Product,
    Category,
)


class CartModelViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    @action(detail=True, methods=["get"])
    def cart_list(self, request):
        pass

    @action(detail=True, methods=["get"])
    def cart_add(self, request):
        pass

    @action(detail=True, methods=["get"])
    def cart_delete(self, request):
        pass

    @action(detail=True, methods=["get"])
    def cart_update(self, request):
        pass
