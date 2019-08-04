from webshop import views
from django.urls import path

app_name = 'webshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.shop_signup, name='signup'),
    path('login/', views.shop_login, name='login'),
    path('logout/', views.shop_logout, name='logout'),
]