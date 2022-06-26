from django.shortcuts import render


def index(request):
    return render(request, 'dashboard/index.html')


def staff(request):
    return render(request, 'dashboard/staff.html')

def product(request):
    return render(request, 'dashboard/product.html')

def orders(request):
    return render(request, 'dashboard/orders.html')
