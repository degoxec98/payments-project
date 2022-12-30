from rest_framework import viewsets
from .pagination import StandardResultsSetPagination
from .models import Expired_payment
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .serializers import ExpiredPaymentsSerializer


class ExpiredPaymentsViewSet(viewsets.ModelViewSet):
    queryset = Expired_payment.objects.get_queryset().order_by('id')
    serializer_class = ExpiredPaymentsSerializer
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAuthenticated,]
        else:
            permission_classes = [IsAdminUser,]
        return [permission() for permission in permission_classes]