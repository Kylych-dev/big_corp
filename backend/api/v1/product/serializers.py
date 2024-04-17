from rest_framework import serializers
from apps.product.models import (
    Product,
    Category
)


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор заказа"""

    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'title',
            'brand'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name"
        )


'''
    category 
    title 
    brand 
    description 
    slug 
    price 
    image 
    available 
    created_at 
    updated_at 
    discount 
    
    
    
    name 
    parent 
    slug 
    created_at 
    
    
'''