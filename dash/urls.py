from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('staff', views.staff, name='dash-staff'),
    path('products', views.product, name='dash-product'),
    path('orders', views.orders, name='dash-orders')
]
