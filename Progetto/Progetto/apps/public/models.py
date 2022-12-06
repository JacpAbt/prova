# Import the necessary modules and classes
from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
import os

# Create the models for the application

# This model defines a merchant, with fields for the country code, date created,
# merchant name, and an admin user
class Merchant(models.Model):
    country_code = CountryField(blank_label='(select country)')
    created_at = models.DateField(auto_now_add=True, null=True)
    merchant_name = models.CharField(max_length=200, null=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    # This method returns the merchant name when the object is printed
    def __str__(self):
        return self.merchant_name

# This model defines a coffee plant type, with fields for the plant name and origin
class CoffeePlantType(models.Model):
    name = models.CharField(max_length=50, null=True)
    origin = models.CharField(max_length=100)

    # This method returns the plant name when the object is printed
    def __str__(self):
        return self.name

# This model defines a process, with a field for the process name
class Process(models.Model):
    name = name = models.CharField(max_length=20, null=True)

    # This method returns the process name when the object is printed
    def __str__(self):
        return self.name

    # This meta class specifies that the plural form of the model name should be "Processes"
    class Meta:
        verbose_name_plural = "Processes"

# This model defines a coffee, with various fields for information about the coffee
class Coffee(models.Model):
    # This is the primary key field, with an auto-incrementing big integer
    id = models.BigAutoField(primary_key=True)
    # Fields for the coffee name, producer, seller, and seller ID (foreign key to the Merchant model)
    name = models.CharField(max_length=200, null=True)
    producer = models.CharField(max_length=200, null=True, blank = True)
    producer_2 = models.CharField(max_length=200, null=True, blank=True)
    seller = models.CharField(max_length=200, null=True)
    seller_id = models.ForeignKey(Merchant, on_delete=models.CASCADE, null=True)
    # Fields for the coffee origin, including country and area
    origin_country = models.CharField(max_length=200, null=True)
    origin_country_2 = models.CharField(max_length=200, null=True, blank=True)
    origin_area = models.CharField(max_length=200, null=True, blank=True)
    origin_area_2 = models.CharField(max_length=200, null=True, blank=True)
    # Many-to-many field for the process and varieties (using foreign keys to the Process and CoffeePlantType models)
    process = models.ManyToManyField(Process)
    tasting_notes = models.CharField(max_length=200, null=True, blank = True)
    varieties = models.ManyToManyField(CoffeePlantType)
    is_it_speciality = models.BooleanField(null=True)
    toast_level = models.IntegerField(null=True, blank = True)
    is_it_available = models.BooleanField(null=True)
    how_many_are_available = models.IntegerField(null=True, blank = True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank = True)
    url_to_product = models.CharField(max_length=100, null=True)
    coffee_image=models.ImageField(upload_to='Progetto/static/theme/assets/img/Coffee/' , null=True, blank = True)
    description = models.CharField(max_length=500, null=True, blank=True)
    
    def imagename(self):
        return os.path.basename(self.coffee_image.name)

    # This method returns a comma-separated list of the processes for the coffee
    def processes(self):
        return ', '.join([str(c) for c in self.process.all()])

    # This method returns a comma-separated list of the plant varieties for the coffee
    def plant_varieties(self):
        return ', '.join([str(c) for c in self.varieties.all()])

    # This method returns the coffee name when the object is printed
    def __str__(self):
        return self.name