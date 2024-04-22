from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404
from drf_yasg import openapi

from apps.cart.cart_session import Cart
from apps.product.models import ProductProxy


class CartModelViewSet(viewsets.ViewSet):
    @action(detail=True, methods=["get"])
    def cart_list(self, request):
        cart = Cart(request)
        serialized_cart = cart.serialize_cart()
        return Response(serialized_cart)

    @action(detail=True, methods=["post"])
    def cart_add(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        product = get_object_or_404(ProductProxy, pk=product_id)
        cart = Cart(request)
        cart.add(product, quantity)
        cart.serialize_cart()
        return Response(
            {'message': 'Product added to cart successfully'},
            status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["post"])
    def cart_delete(self, request):
        product_id = request.data.get('product_id')
        cart = Cart(request)
        cart.delete_product(product_id)
        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        pass

    @action(detail=True, methods=["update"])
    def cart_update(self, request):
        pass


'''

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)
        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_qty, 'total': cart_total})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)
        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty': cart_qty, 'total': cart_total})
        return response

'''