from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (BrandCountViewSet, BrandViewSet, CarColorViewSet,
                    CarModelViewSet, ColorCountViewSet, OrderModelViewSet)

router = DefaultRouter()

router.register(
    'order',
    OrderModelViewSet,
    basename='order'
)
router.register(
    'color',
    CarColorViewSet,
    basename='color',
)
router.register(
    'brand',
    BrandViewSet,
    basename='brand'
)
router.register(
    'model',
    CarModelViewSet,
    basename='model'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path(
        'v1/count/color/',
        ColorCountViewSet.as_view({'get': 'list'}),
        name='color_count'),
    path(
        'v1/count/brand/',
        BrandCountViewSet.as_view({'get': 'list'}),
        name='brand_count')
]
