from django.urls import path, include

from rest_framework import routers

from .api import (
    ActivateProductViewSet,
    CancelProductActivationViewSet,
    AdminProductActivationViewSet
)

from .views import IndexView


urlpatterns = [
    path('product/activate', ActivateProductViewSet.as_view({'post': 'create'})),
    path(r'product/activate/<int:pk>', CancelProductActivationViewSet.as_view({'delete': 'destroy'})),
    path(r'product/activation/approve/<int:pk>', AdminProductActivationViewSet.as_view({'post': 'approve'})),
    path(r'product/activation/reject/<int:pk>', AdminProductActivationViewSet.as_view({'post': 'reject'})),
    path('', IndexView.as_view())
]
