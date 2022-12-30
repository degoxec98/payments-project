from rest_framework import routers
from .views import PaymentUserViewSet


router=routers.DefaultRouter()

router.register(r'payment-user', PaymentUserViewSet)

urlpatterns=[]

urlpatterns += router.urls