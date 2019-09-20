from rest_framework import serializers
from django.contrib.auth.models import User
from webshop.models import Shop, Product, ProductInfo, Order


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


class ShopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Shop
        fields = ('id', 'name', 'url', 'products',)
        depth = 1


class ProductInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductInfo
        fields = ('name', 'quantity', 'price', 'price_rrc', 'shops')
        depth = 1


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'category', 'productinfo')
        depth = 1


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'dt', 'status', 'user', 'orderitem_set')
        depth = 1