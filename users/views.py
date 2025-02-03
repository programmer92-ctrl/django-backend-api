from django.shortcuts import render
from django.http import JsonResponse
from .serializers import UserSerializer
from .forms import UserRegisterForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.set_password(form.cleaned_data['password'])
            user.save()
            return JsonResponse({'Message': 'User added successfully'})
    else:
        form = UserRegisterForm()
    return JsonResponse({'Message': 'Error'})

def get_user_by_username(request, username):
    user = User.objects.filter(username=username).first()
    serializer = UserSerializer(user)
    serialized_data = serializer.data
    return JsonResponse(serialized_data)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user and user.check_password(user):
            return JsonResponse({'Message': 'User loggedin successfully'})
        else:
            return JsonResponse({'Message': 'User/Password invalid'})
        return JsonResponse({'Message': 'Database error'})
