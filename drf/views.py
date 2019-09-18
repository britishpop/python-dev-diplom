from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from webshop.models import Shop, Product, Order
from .serializers import UserSerializer, ShopSerializer, ProductSerializer, OrderSerializer

# Create your views here.


class UsersView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)


class ShopsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Shop.objects.all()
        serializer = ShopSerializer(queryset, many=True)
        return Response(serializer.data)


class ProductsView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class OrdersView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)


class UserView(APIView):

    def get(self, request, pk, *args, **kwargs):
        queryset = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(queryset)
        return Response(serializer.data)


class ShopView(APIView):

    def get(self, request, pk, *args, **kwargs):
        queryset = get_object_or_404(Shop, pk=pk)
        serializer = ShopSerializer(queryset)
        return Response(serializer.data)


class ProductView(APIView):

    def get(self, request, pk, *args, **kwargs):
        queryset = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(queryset)
        return Response(serializer.data)


class OrderView(APIView):

    def get(self, request, pk, *args, **kwargs):
        queryset = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(queryset)
        return Response(serializer.data)
