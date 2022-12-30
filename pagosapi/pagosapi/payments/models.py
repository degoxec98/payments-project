from django.db import models
from user.models import User
from services.models import Service

# Create your models here.

class Payment_user(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    paymentDate = models.DateField(auto_now_add=True)
    expirationDate = models.DateField()

    class Meta:
        db_table = "payment_user"
