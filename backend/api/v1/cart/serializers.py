from rest_framework import serializers

class CartItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    title = serializers.CharField()
    quantity = serializers.IntegerField()
