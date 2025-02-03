# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
from .forms import CartForm
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import CartSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'Message', 'Successfully added to cart'})
        else:
            form = CartForm()
    return JsonResponse({'Message', 'Error'})

def get_cart(request):
    if request.method == 'GET':
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return JsonResponse(serializer.data, safe=False)

def get_user_cart(request, user):
    if request.method == 'GET':
        cart = Cart.objects.filter(user=user).first()
        serializer = CartSerializer(cart, many=True)
        return JsonResponse(serializer.data, safe=False)

def delete_item_from_cart(request, pk):
    cart_item = Cart.objects.filter(pk=pk).first()
    cart_item.delete()
    return JsonResponse({'Message': 'Successfully deleted item from cart'})
