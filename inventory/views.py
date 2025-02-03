from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import *
from .forms import InventoryForm
from django.shortcuts import get_list_or_404, get_object_or_404
from .serializers import InventorySerializer
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

def items(request):
    if request.method == 'GET':
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True)
        return JsonResponse(serializer.data, safe=False)

def item(request, item_id):
    if request.method == 'GET':
        item = get_object_or_404(Inventory, pk=item_id)
        serializer = InventorySerializer(item)
        serialized_data = serializer.data
        return JsonResponse(serialized_data)

@csrf_exempt
def add(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'Message': 'Successfully added item to inventory'})
        else:
            form = InventoryForm()
    return JsonResponse({'Message': 'Error'})

@csrf_exempt
def update(request, item_id):
    item = Inventory.objects.filter(pk=item_id).first()
    if request.method == 'UPDATE':
        form = InventoryForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return JsonResponse({'Message': 'Successfully updated item'})
        else:
            form = InventoryForm()
    return JsonResponse({'Message': 'Error'})

def delete(request, item_id):
    item = Inventory.objects.filter(pk=item_id).first()
    item.delete()
    return JsonResponse({'Message': 'Successfully deleted item'})
