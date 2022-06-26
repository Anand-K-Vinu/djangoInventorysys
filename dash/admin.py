from django.contrib import admin
from .models import product, order
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = 'Xventory AdminPanel '


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')
    list_filter = ['category']


admin.site.register(product, ProductAdmin),
admin.site.register(order)
