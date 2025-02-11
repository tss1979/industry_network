from rest_framework import serializers
from network.models import Plant, Retail, Entrepreneur


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = '__all__'


class EntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreneur
        fields = '__all__'
