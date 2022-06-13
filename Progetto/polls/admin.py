from django.contrib import admin
from .models import  Coffee, Merchant, User

# Register your models here.
admin.site.register(User)
admin.site.register(Merchant)
admin.site.register(Coffee)