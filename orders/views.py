from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
from .forms import OrderForm
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import OrderSerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def orders(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

def order(request, order_id):
    if request.method == 'GET':
        order = get_object_or_404(Order, pk=order_id)
        serializer = OrderSerializer(order)
        serialized_data = serializer.data
        return JsonResponse(serialized_data)

@csrf_exempt
def add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'Message': 'Successfully added order'})
        else:
            form = OrderForm()
    return JsonResponse({'Message': 'Error'})

@csrf_exempt
def update(request, order_id):
    if request.method == 'UPDATE':
        order = Order.objects.filter(pk=order_id).first()
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return JsonResponse({'Message': 'Successfully updated order'})
        else:
            form = OrderForm()
    return JsonResponse({'Message': 'Error'})

def delete(request, order_id):
    order = Order.objects.filter(pk=order_id).first()
    order.delete()
    return JsonResponse({'Message': 'Successfully deleted order'})
