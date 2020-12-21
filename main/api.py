from rest_framework import serializers, viewsets
from rest_framework import mixins

from .models import DebitoAutomatico

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class DebitoAutomaticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebitoAutomatico 
        fields = ['conta',]


class ActivateProductViewSet(viewsets.GenericViewSet):
    serializer_class = DebitoAutomaticoSerializer
    http_method_names = ['POST']


class DebitoAutomaticoViewSet(viewsets.ModelViewSet):
    queryset = DebitoAutomatico.objects.all()
    serializer_class = DebitoAutomaticoSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def foo(request):
    return Response({}, status=status.HTTP_201_CREATED)
