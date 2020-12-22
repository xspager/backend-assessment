from django.urls import path, include

from rest_framework import routers

from .api import ActivateProductViewSet, CancelProductActivationViewSet


urlpatterns = [
    path('product/activate', ActivateProductViewSet.as_view({'post': 'create'})),
    path(r'product/activate/<int:pk>', CancelProductActivationViewSet.as_view({'delete': 'destroy'})),
]
