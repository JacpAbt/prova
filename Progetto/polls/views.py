from django.shortcuts import render
import random
from .models import Coffee
from django.template import loader

# Create your views here.

def coffees(request):
    all_coffees = []
    for coffee in Coffee.objects.all():
        all_coffees.append(coffee)
    output = ', '.join([str(p) for p in Coffee.objects.all()])
    template = loader.get_template('polls/index.html')
    html = "<html><body>%s</body></html>" % output
    context = {
        'all_coffees': all_coffees,
    }
    return render(request, 'polls/index.html', context)

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')