from django.contrib import admin
from .models import  UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'mail', 'country_code',)

    list_filter = ('country_code',)


admin.site.register(UserProfile, UserProfileAdmin)

