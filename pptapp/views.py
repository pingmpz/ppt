from django.shortcuts import render
from .models import Employee, Order, Serial, Path

def index(request):
    context = {
    }
    return render(request, 'index.html', context)

def new_workorder(request):
    context = {
    }
    return render(request, 'new_workorder.html', context)

def order_master(request):
    orders = Order.objects.all()
    items = []
    for order in orders:
        serials = Serial.objects.filter(order=order)
        items.append(len(serials))
    context = {
        'orders' : orders,
        'items' : items,
    }
    return render(request, 'order_master.html', context)

def emp_master(request):
    context = {
    }
    return render(request, 'emp_master.html', context)

def fg_master(request):
    context = {
    }
    return render(request, 'fg_master.html', context)
