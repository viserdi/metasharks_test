from django_filters import rest_framework as filters

from order.models import Order


class BrandFilter(filters.FilterSet):
    """Фильтр поиска по Марке авто."""

    brand = filters.CharFilter(field_name='model__brand__name',)

    class Meta:
        model = Order
        fields = ('brand',)
