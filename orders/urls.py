from django.urls import path
from . import views

urlpatterns = [

    path('orders/orders', views.orders, name='orders'),
    path('orders/order/<int:order_id>', views.order, name='order'),
    path('order/add/', views.add, name='add'),
    path('orders/update/<int:order_id>', views.update, name='update'),
    path('orders/delete/<int:order_id>', views.delete, name='delete')

]
