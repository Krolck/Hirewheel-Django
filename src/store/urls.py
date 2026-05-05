from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path("", views.store),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/checkout/', views.checkout, name = 'checkout')

]