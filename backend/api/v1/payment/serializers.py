from rest_framework import serializers
from apps.payment.models import (
    ShippingAddress,
    Order,
    OrderItem
)

'''
    full_name
    email
    street_address
    apartment_address
    user
    country
    city
    zip_code 
'''


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = (
            'id',
            'full_name',
            'email',
            'street_address',
            'user',
            'country'
            'city'
            'zip_code'
        )


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            "id",
            "name",
            "slug"
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "id",
            "name",
            "slug"
        )


'''
ShippingAddress

Order

OrderItem


    full_name
    email
    street_address
    apartment_address
    user
    country
    city
    zip_code 
    
    user
    shipping_address
    amount
    created_at
    updated_at
    paid
    discount 

    order
    product
    price
    quantity
    user 
'''