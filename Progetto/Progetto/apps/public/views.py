from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from .models import Coffee


def index(request: HttpRequest) -> HttpResponse:
    print(request.user)
    return render(request, 'index.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')

def coffees(request: HttpRequest) -> HttpResponse:
    coffee_list = Coffee.objects.all()
    return render(request, 'Coffees.html',
    {'coffee_list': coffee_list},)

def standard_coffee(request, coffee_id):
    try:
        # Look up the coffee by ID 
        coffee = Coffee.objects.get(id=coffee_id)
    except Coffee.DoesNotExist:
        # Handle the case where the coffee does not exist
        return redirect('coffees')
    # Redirect to the coffee_by_name URL pattern
    return render(request, 'standard_coffee.html', {'coffee': coffee})

