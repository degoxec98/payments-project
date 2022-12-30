from rest_framework import serializers
from .models import Expired_payment


class ExpiredPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expired_payment
        fields = '__all__'