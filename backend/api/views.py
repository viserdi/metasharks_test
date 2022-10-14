from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets

from cars.models import Brand, CarColor, CarModel
from order.models import Order

from .filters import BrandFilter
from .serializers import (BrandCountSerializer, BrandSerializer,
                          CarColorSerializer, CarModelSerializer,
                          ColorCountSerializer, OrderGETSerializer,
                          OrderPOSTSerializer)


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter,)
    ordering_fields = ('count',)
    filterset_class = BrandFilter

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return OrderGETSerializer
        return OrderPOSTSerializer


class CarColorViewSet(viewsets.ModelViewSet):
    serializer_class = CarColorSerializer
    queryset = CarColor.objects.all()


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class CarModelViewSet(viewsets.ModelViewSet):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.all()


class ColorCountViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ColorCountSerializer
    queryset = CarColor.objects.all()
    pagination_class = None


class BrandCountViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BrandCountSerializer
    queryset = Brand.objects.all()
    pagination_class = None
