from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from webshop.models import Shop, Product, Order
from .serializers import UserSerializer, ShopSerializer, ProductSerializer, OrderSerializer

# Create your views here.

# User classes

class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Shop classes

class ShopsView(generics.ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopCreateView(generics.CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ShopDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

# Product classes

class ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Order classes

class OrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteView(generics.DestroyAPIView):
    lookup_field = 'pk'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
