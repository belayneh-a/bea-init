from django.db import models
from momoapi.momoapi_q2 import views

class RequestToPay(models.Model):
    api_user = models.CharField(max_length=50)
    api_key = models.CharField(max_length=300)
    payer_info = models.CharField(max_length=100)
    dis_amount = models.CharField(max_length=20)
    trans_status = models.CharField(max_length=100)
    trans_time = models.DateTimeField(auto_now_add=True)

# was supposed to make authomatic request

    def __self__(self):
        momoapi_q2.requestopay()

