from django.db import models
from payments.models import Payment_user

# Create your models here.
class Expired_payment(models.Model):
    payment_user_id = models.ForeignKey(Payment_user, on_delete=models.CASCADE)
    penalty_fee_amount = models.CharField(max_length=150)
    class Meta:
        db_table = "expired_payment"