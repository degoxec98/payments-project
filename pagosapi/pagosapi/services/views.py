from .models import Service
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import ServiceSerializer
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    pagination_class= StandardResultsSetPagination

    def get_permissions(self):
        if self.action not in ['destroy','partial_update','update','create']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]

        return [permission() for permission in permission_classes]


class GetAllServiceView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get(self, request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)