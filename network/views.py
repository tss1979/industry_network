from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from network.serializers import PlantSerializer, RetailSerializer, EntrepreneurSerializer
from network.models import Plant, Retail, Entrepreneur
from network.permissions import UserIsActivePermission


class PlantViewSet(viewsets.ModelViewSet):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class RetailViewSet(viewsets.ModelViewSet):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()
    permission_classes = [IsAuthenticated, UserIsActivePermission]


class EntrepreneurViewSet(viewsets.ModelViewSet):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
    permission_classes = [IsAuthenticated, UserIsActivePermission]
