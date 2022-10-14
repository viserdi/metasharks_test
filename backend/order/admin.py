from django.contrib import admin

from .models import Order


@admin.register(Order)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'color', 'model', 'count', 'date', )
    fields = ('model', 'color', 'count', 'date')
