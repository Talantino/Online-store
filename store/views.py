from django.shortcuts import render
from .models import (
Category,
Product,
Order,
Customer
)


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html',)
