from django import forms
from .models import Cart

class CartForm(forms.ModelForm):
    model = Cart
    fields =['user' 'item_name', 'item_description', 'item_price', 'item_image']
