from . import views
from django.urls import include, path
from .models import Coffee

app_name='public'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('coffees', views.coffees, name='coffees'),
]


coffee_list = Coffee.objects.all()
for coffee in coffee_list:
    coffee_name = coffee.name
    coffee_url_name = coffee.name.replace(' ', '_')
    urlpatterns.append(path('coffees/'+str(coffee_url_name), views.standard_coffee, name=coffee_name))

