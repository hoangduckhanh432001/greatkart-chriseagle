
from django.contrib import admin

# Register your models here.
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('product_name',)}
    list_display = ['product_name','slug','description','price','stock','is_available','category',]

admin.site.register(Product, ProductAdmin)