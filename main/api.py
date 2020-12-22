from rest_framework import serializers, viewsets
from rest_framework import mixins

from .models import Activation

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.http import require_http_methods, require_POST


class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activation 
        fields = ['id', 'partner', 'customer']

@permission_classes([IsAuthenticated])
class ActivateProductViewSet(viewsets.ModelViewSet):
    serializer_class = ActivationSerializer
    queryset = Activation.objects.none()

class CancelProductActivationViewSet(viewsets.ModelViewSet):
    serializer_class = ActivationSerializer
    queryset = Activation.objects.filter(status=Activation.StatusActivation.REQUESTED)
