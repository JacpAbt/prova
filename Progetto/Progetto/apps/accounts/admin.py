from django.contrib import admin
from .models import  Coffee, Merchant, UserProfile, CoffeePlantType, Process

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'mail', 'country_code',)

    list_filter = ('country_code',)


class MerchantAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at')
    list_display = ('country_code', 'merchant_name')

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'seller', 'producer', 'origin_country', 'toast_level', 'processes', 'plant_varieties',
                        'tasting_notes', 'is_it_speciality')
    fieldsets = (
        (None, {
            'fields' : ('name','seller','seller_id','origin_country','process','is_it_speciality','is_it_available',
                        'url_to_product',)
        }),
        ('More informations', {
            'classes': ('collapse',),
            'fields' : ('producer', 'tasting_notes', 'varieties', 'toast_level', 'how_many_are_available', 'origin_country_2',
                        'origin_area', 'origin_area_2', 'price', 'producer_2')
        }),
    )
    list_filter = ('seller', 'origin_country', 'process')


    
                
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Merchant)
admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(CoffeePlantType)
admin.site.register(Process)
