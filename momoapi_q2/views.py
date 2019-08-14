from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import requests
from .models import RequestToPay
from .serializers import RequestToPaySerializer

class MomoRequest(APIView):

    def requestopay(self,request):
        x_request = RequestToPay.object.all()
        serialize = RequestToPaySerializer(x_request, many=False)
        return render(serialize.data)

