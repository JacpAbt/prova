from django.shortcuts import render
from .models import Coffee
from django.template import loader
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name= 'accounts/profile.html'

def coffees(request):
    all_coffees = []
    for coffee in Coffee.objects.all():
        all_coffees.append(coffee)
    output = ', '.join([str(p) for p in Coffee.objects.all()])
    template = loader.get_template('index.html')
    html = "<html><body>%s</body></html>" % output
    context = {
        'all_coffees': all_coffees,
    }
    return render(request, 'index.html', context)

def index(request):
    print(request.user)
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

