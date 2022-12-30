from rest_framework import serializers
from .models import Payment_user


class PaymentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_user
        fields = '__all__'
        read_only_fields = 'user_id', 'payment_date', 'expiration_date'