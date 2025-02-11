from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from network.serializers import PlantSerializer, RetailSerializer, EntrepreneurSerializer
from network.models import Plant, Retail, Entrepreneur
from network.permissions import UserIsAdminPermission

# Create your views here.


class LevelElementViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, UserIsAdminPermission]

    @action(detail=True, methods=("PATCH", ))
    def reset_credit(self, pk):
        element = get_object_or_404(self.queryset, pk)
        if element:
            element.credit = 0
            element.save()
        serializer = self.get_serializer(element)
        return Response(data=serializer.data)


class PlantViewSet(LevelElementViewSet):
    serializer_class = PlantSerializer
    queryset = Plant.objects.all()


class RetailViewSet(LevelElementViewSet):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()


class EntrepreneurViewSet(LevelElementViewSet):
    serializer_class = EntrepreneurSerializer
    queryset = Entrepreneur.objects.all()
