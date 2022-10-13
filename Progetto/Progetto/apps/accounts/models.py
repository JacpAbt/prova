from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(max_length=200, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    country_code = CountryField()
    mail = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.user_name
class Merchant(models.Model):
    country_code = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    merchant_name = models.CharField(max_length=200, null=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.merchant_name

class CoffeePlantType(models.Model):
    name = models.CharField(max_length=50, null=True)
    origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Process(models.Model):
    name = name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Processes"

class Coffee(models.Model):
    name = models.CharField(max_length=200, null=True)
    producer = models.CharField(max_length=200, null=True, blank = True)
    producer_2 = models.CharField(max_length=200, null=True, blank=True)
    seller = models.CharField(max_length=200, null=True)
    seller_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    origin_country = models.CharField(max_length=200, null=True)
    origin_country_2 = models.CharField(max_length=200, null=True, blank=True)
    origin_area = models.CharField(max_length=200, null=True, blank=True)
    origin_area_2 = models.CharField(max_length=200, null=True, blank=True)
    process = models.ManyToManyField(Process)
    tasting_notes = models.CharField(max_length=200, null=True, blank = True)
    varieties = models.ManyToManyField(CoffeePlantType)
    is_it_speciality = models.BooleanField(null=True)
    toast_level = models.IntegerField(null=True, blank = True)
    is_it_available = models.BooleanField(null=True)
    how_many_are_available = models.IntegerField(null=True, blank = True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank = True)
    url_to_product = models.CharField(max_length=100, null=True)
    image_coffee=models.ImageField(null=True, blank = True)

    def processes(self):
        return ', '.join([str(c) for c in self.process.all()])

    def plant_varieties(self):
        return ', '.join([str(c) for c in self.varieties.all()])
    
    def __str__(self):
        return self.name