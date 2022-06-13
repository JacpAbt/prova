from django.db import models
from django.forms import CharField, DateField

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True),
    full_name = CharField(max_length=200),
    created_at = DateField(),
    country_code = models.IntegerField()

class Merchant(models.Model):
    id = models.BigAutoField(primary_key=True),
    country_code = models.IntegerField(),
    merchant_name = CharField(max_length=None),
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Coffee(models.Model):
    id = models.BigAutoField(primary_key=True),
    name = models.CharField(max_length=200),
    producer = models.CharField(max_length=200),
    producer_id = models.ForeignKey(Merchant, on_delete=models.CASCADE),
    origin = models.CharField(max_length=200),
    is_it_speciality = models.BooleanField(),
    toast_level = models.IntegerField(),
    is_it_available = models.BooleanField()
