from django.urls import path
from . import views

urlpatterns = [

    path('cart/add/', views.add, name='add'),
    path('cart/get_user_cart/<str:user>', views.get_user_cart, name='get_user_cart'),
    path('cart/delete_item_from_cart/<int:pk>', views.delete_item_from_cart, name='delete_item_from_cart'),

]

