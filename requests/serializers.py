from rest_framework import serializers
from .models import *


class RequestsOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('name',
                  'mail',
                  'message',
                  'project_version',
                  'user_agent',
                  'screen_resolution',
                  'browser_language',
                  'timezone',
                  'cookie')

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class RequestsRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ('source',
                  'rate_value',
                  'project_version',
                  'user_agent',
                  'screen_resolution',
                  'browser_language',
                  'timezone',)

    def create(self, validated_data):
        return Rate.objects.create(**validated_data)


class RequestsFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('source',
                  'rate_message',
                  'project_version',
                  'user_agent',
                  'screen_resolution',
                  'browser_language',
                  'timezone',)

    def create(self, validated_data):
        return Feedback.objects.create(**validated_data)
