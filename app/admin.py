from django.contrib import admin
from .models import card,product_details,cart_model

class cardadmin(admin.ModelAdmin):
    list_display = ('category','model','brand','price')
admin.site.register(card,cardadmin)
# Register your models here.

class product_details_admin(admin.ModelAdmin):
    list_display = ("model","specs")
admin.site.register(product_details,product_details_admin)

class cart_admin(admin.ModelAdmin):
    list_display = ('category','model','brand','price')
admin.site.register(cart_model,cart_admin)