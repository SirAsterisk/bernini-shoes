from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'price', 'created', 'updated']
	list_filter = ['created', 'updated']
	list_editable = ['price',]
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)