from django.contrib import admin
from . import models
from django import forms

# Register your models here.


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_code','category','address','place',]
    list_per_page = 3
    search_fields = ['customer_name__istartswith','customer_code__iendswith']


@admin.register(models.Uom)
class UomAdmin(admin.ModelAdmin):
    list_display= ['unit','unit_type','unit_code']

@admin.register(models.CustomerPo)
class CustomerPoAdmin(admin.ModelAdmin):
    # autocomplete_fields = ['customer_name']  
    # inlines = [CustomerPoItemInline]
    list_display = ['customer_po_number','customer_code','customer_name']
    # list_display = '__all__'
    # list_editable = ['status']
    list_per_page = 10
    list_select_related = ['customer_name']
    search_fields = ['customer_po_number__istartswith','status__istartswith']

    def customer_address(self,customerpo):
        return customerpo.customer_name.address
