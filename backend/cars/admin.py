from django.contrib import admin

from .models import Brand, CarColor, CarModel


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(CarColor)
class CarColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'name')
