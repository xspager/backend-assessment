from django.urls import path, include

from rest_framework import routers

#from . import views
from .api import DebitoAutomaticoViewSet, foo

#router = routers.DefaultRouter()
#router.register(r'activate', ActivateProductViewSet)

urlpatterns = [
    #path('activate', views.request_activation, name="product-activate")
    #path('products/', include(router.urls)),
    path('product/activate', foo, name="product-activate")
]
