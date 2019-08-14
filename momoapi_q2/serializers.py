from rest_framework import serializers
from .models import RequestToPay


class RequestToPaySerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestToPay
        fields = {'api_user', 'api_key', 'payer_info', 'dis_amount'}