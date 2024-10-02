from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import UnitMeasurement, ProductGroup, Product


@admin.register(UnitMeasurement)
class UnitMeasurementAdmin(admin.ModelAdmin):
  pass


@admin.register(ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
  pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_display = ['code', 'name']