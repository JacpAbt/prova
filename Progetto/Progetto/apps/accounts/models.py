from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_name = models.CharField(max_length=200, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)
    country_code = CountryField()
    mail = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.user_name
