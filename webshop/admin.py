from django.contrib import admin
from .models import Profile, Shop, Category, Product, ProductInfo, Parameter,\
                    ProductParameter, Order, OrderItem, Contact, Cart, CartItem

# Register your models here.

admin.site.register(Profile)
admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductInfo)
admin.site.register(Parameter)
admin.site.register(ProductParameter)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Contact)
admin.site.register(Cart)
admin.site.register(CartItem)