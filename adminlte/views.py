
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# from .models import Product

# Create your views here.

def index(request):
    return render(request, 'administrator/index.html')