from rest_framework import serializers
from .models import *

class RequestsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('name', 'mail', 'message')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)