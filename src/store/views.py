from django.shortcuts import render

# Create your views here.
from .models import Item

def store(request):
    items = Item.objects.all()
    return render(request, 'store/store.html', {'items': items})