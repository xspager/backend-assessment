from rest_framework import serializers, viewsets
from rest_framework import mixins

from .models import Activation

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ActivationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activation 
        fields = ['conta',]


class ActivateProductViewSet(viewsets.GenericViewSet):
    serializer_class = Activation
    http_method_names = ['POST']


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def activation_view(request):
    return Response({}, status=status.HTTP_201_CREATED)
