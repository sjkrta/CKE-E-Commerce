from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {'Products':Products.objects.all()})

def product_detail(request, pk):
    return render(request, 'product_detail.html', {'Product':Products.objects.get(id=pk)})