from django.urls import re_path
from . import views


app_name = 'order_create'
urlpatterns = [
    re_path(r'^create/$', views.OrderCreate, name='order_create'),
]

