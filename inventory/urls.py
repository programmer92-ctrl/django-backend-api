from django.urls import path
from . import views

urlpatterns = [

    path('inventory/items', views.items, name='items'),
    path('inventory/item/<int:item_id>', views.item, name='item'),
    path('inventory/add/', views.add, name='add'),
    path('inventory/update/<int:item_id>', views.update, name='update'),
    path('inventory/delete/<int:item_id>', views.delete, name='delete')

]
