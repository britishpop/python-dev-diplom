from drf import views
from django.urls import path

app_name = 'drf'

urlpatterns = [
    path('users/', views.UsersView.as_view(), name='users'),
    path('shops/', views.ShopsView.as_view(), name='shops'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('users/<int:pk>/', views.UserView.as_view(), name='user'),
    path('shops/<int:pk>/', views.ShopView.as_view(), name='shop'),
    path('products/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('orders/<int:pk>/', views.OrderView.as_view(), name='order'),
]
