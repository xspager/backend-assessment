from rest_framework import serializers, viewsets

from .models import Activation

from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.views.decorators.http import require_http_methods, require_POST


class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activation 
        fields = ['id', 'partner', 'customer']

@permission_classes([IsAuthenticated])
class ActivateProductViewSet(viewsets.ModelViewSet):
    serializer_class = ActivationSerializer
    queryset = Activation.objects.none()

@permission_classes([IsAuthenticated])
class CancelProductActivationViewSet(viewsets.ModelViewSet):
    serializer_class = ActivationSerializer
    queryset = Activation.objects.filter(status=Activation.StatusActivation.REQUESTED)

@permission_classes([IsAuthenticated, IsAdminUser])
class AdminProductActivationViewSet(viewsets.ModelViewSet):
    serializer_class = ActivationSerializer
    queryset = Activation.objects.filter(status=Activation.StatusActivation.REQUESTED)

    def approve(self, request, pk=None):
        activation = self.get_object()
        activation.approve()

        serializer = self.get_serializer(activation)
        return Response(serializer.data)

    def reject(self, request, pk=None): 
        activation = self.get_object()
        activation.reject()

        serializer = self.get_serializer(activation)
        return Response(serializer.data)

