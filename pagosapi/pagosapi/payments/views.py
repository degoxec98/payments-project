from django.shortcuts import render

from rest_framework import filters
from rest_framework import viewsets
from .pagination import StandardResultsSetPagination
from .models import Payment_user
from rest_framework.permissions import AllowAny,IsAdminUser
from .serializers import PaymentUserSerializer

# Create your views here.
class PaymentUserViewSet(viewsets.ModelViewSet):
    queryset = Payment_user.objects.all()
    serializer_class = PaymentUserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['user_id', 'service_id', 'paymentDate']
    http_method_names=['get','post']
    
    def get_permissions(self):
        if self.action in ["list", "create"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]