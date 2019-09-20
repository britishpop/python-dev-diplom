from drf import views
from django.urls import path

app_name = 'drf'

urlpatterns = [
    path('users/', views.UsersView.as_view(), name='users'),
    path('users/<int:pk>/', views.UserView.as_view(), name='user_detail'),
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/delete/<int:pk>/', views.UserDeleteView.as_view(), name='user_delete'),
    path('shops/', views.ShopsView.as_view(), name='shops'),
    path('shops/<int:pk>/', views.ShopView.as_view(), name='shop_detail'),
    path('shops/create/', views.ShopCreateView.as_view(), name='shop_create'),
    path('shops/delete/<int:pk>/', views.ShopDeleteView.as_view(), name='shop_delete'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductView.as_view(), name='product_detail'),
    path('products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('orders/<int:pk>/', views.OrderView.as_view(), name='order_detail'),
    path('orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('orders/delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
]
