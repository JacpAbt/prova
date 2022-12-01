from django.shortcuts import render
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

def standard_coffee(request: HttpRequest, coffee_id) -> HttpResponse:
    coffee = Coffee.objects.get(pk=coffee_id)
    return render(request, 'standard_coffee.html',
            {'coffee': coffee},)

