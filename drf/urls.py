from drf import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'shops', views.ShopViewSet, basename='shop')
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'orders', views.OrderViewSet, basename='order')
router.register(r'carts', views.CartViewSet, basename='cart')

app_name = 'drf'

urlpatterns = router.urls