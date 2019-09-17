from drf import views
from django.urls import path

app_name = 'drf'

urlpatterns = [
    path('', views.index, name='index'),
]