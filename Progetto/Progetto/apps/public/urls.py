from . import views
from django.urls import include, path

app_name='public'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('coffees', views.coffees, name='coffees'),
    path('coffees/<int:coffee_id>/', views.standard_coffee, name='coffee')
]




