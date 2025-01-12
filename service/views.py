from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView

from service.serializers import (
    RequestsOrderSerializer,
    RequestsRateSerializer,
    RequestsFeedbackSerializer
)
from service.utils import telepush_send


@permission_classes((permissions.AllowAny,))
class OrderCreateView(APIView):
    """
    API endpoint that allows Orders to be created
    """
    def post(self, request):
        request_data = request.data.get('request')

        serializer = RequestsOrderSerializer(data=request_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            order_data = serializer.data
            telepush_send(order_data)

        return JsonResponse({"success": "Order created successfully"})


@permission_classes((permissions.AllowAny,))
class RateCreateView(APIView):
    """
    API endpoint that allows Rate to be created
    """
    def post(self, request):
        request_data = request.data.get('request')

        serializer = RequestsRateSerializer(data=request_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return JsonResponse({"success": "Rate created successfully"})


@permission_classes((permissions.AllowAny,))
class FeedbackCreateView(APIView):
    """
    API endpoint that allows Feedback to be created
    """
    def post(self, request):
        request_data = request.data.get('request')

        serializer = RequestsFeedbackSerializer(data=request_data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return JsonResponse({"success": "Feedback created successfully"})

