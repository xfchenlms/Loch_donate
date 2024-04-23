from django.urls import path
from . import views

urlpatterns = [
path('', views.index, name='index'),
path('lochlist/', views.loch_list, name='loch_list'),

path('loch/<int:id>/', views.loch_detail, name= 'loch_detail'),
path('add_to_cart/<int:loch_id>/', views.add_to_cart, name='add_to_cart'),
path('cart/', views.cart, name='cart'),
path('delete_from_cart/<int:cart_item_id>/', views.delete_from_cart, name='delete_from_cart'),
]