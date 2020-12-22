from django.urls import path, include

from rest_framework import routers

from .api import ActivateProductViewSet


urlpatterns = [
    path('product/activate', ActivateProductViewSet.as_view({'post': 'create'})),
]
