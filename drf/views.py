from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from webshop.models import Shop, Product, Order, Cart
from .serializers import UserSerializer, ShopSerializer, ProductSerializer, OrderSerializer, CartSerializer

# Create your views here.

# User classes

class UserViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


# Shop classes

class ShopViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Shop.objects.all()
        shop = get_object_or_404(queryset, pk=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Shop.objects.all()
        shop = get_object_or_404(queryset, pk=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Shop.objects.all()
        shop = get_object_or_404(queryset, pk=pk)
        serializer = ShopSerializer(shop)
        return Response(serializer.data)


# Product classes

class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


# Order classes

class OrderViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Order.objects.all()
        order = get_object_or_404(queryset, pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


# Cart classes

class CartViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        queryset = Cart.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        queryset = Cart.objects.all()
        serializer = CartSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Cart.objects.all()
        cart = get_object_or_404(queryset, pk=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)