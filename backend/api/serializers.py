from django.db.models import Sum
from rest_framework import serializers

from cars.models import Brand, CarColor, CarModel
from order.models import Order


class BrandSerializer(serializers.ModelSerializer):
    """Сериализатор Марки авто."""

    class Meta:
        model = Brand
        fields = '__all__'


class CarColorSerializer(serializers.ModelSerializer):
    """Сериализатор Цвета авто."""

    class Meta:
        model = CarColor
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    """Сериализатор Модели авто."""

    class Meta:
        model = CarModel
        fields = '__all__'


class OrderGETSerializer(serializers.ModelSerializer):
    """Сериализатор для GET Заказа авто."""

    date = serializers.DateField(read_only=False,)
    model = serializers.CharField(source='model.name')
    color = serializers.CharField(source='color.name')
    brand = serializers.CharField(read_only=True, source='model.brand')

    class Meta:
        model = Order
        fields = ('id', 'brand', 'model', 'count', 'color', 'date')


class OrderPOSTSerializer(serializers.ModelSerializer):
    """Сериализатор для POST Заказа авто."""
    class Meta:
        model = Order
        fields = '__all__'


class ColorCountSerializer(serializers.ModelSerializer):
    """Сериализатор количества заказанных авто по цвету."""
    count = serializers.SerializerMethodField()

    class Meta:
        model = CarColor
        fields = ('name', 'count')

    @staticmethod
    def get_count(instance):
        queryset = Order.objects.filter(color=instance)
        return queryset.aggregate(sum=Sum('count')).get('sum') if queryset else 0


class BrandCountSerializer(serializers.ModelSerializer):
    """Сериализатор количества авто по Маркам."""
    count = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ('name', 'count')

    @staticmethod
    def get_count(instance):
        queryset = Order.objects.filter(model__brand=instance)
        return queryset.aggregate(sum=Sum('count')).get('sum') if queryset else 0