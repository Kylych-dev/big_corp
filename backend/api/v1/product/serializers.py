from rest_framework import serializers
from apps.product.models import (
    ProductProxy,
    Product,
    Category
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'category',
            'title',
            'brand',
            'slug'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug"
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