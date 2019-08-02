from webshop import views
from django.urls import path

app_name = 'webshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]