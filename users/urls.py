from django.urls import path
from . import views

urlpatterns = [

    path('user/register', views.register, name='register'),
    path('user/get_user_by_username/<str:username>', views.get_user_by_username, name='get_user_by_username'),
    path('user/login', views.login, name='login'),

]
