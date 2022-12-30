from rest_framework import routers
from .views import ExpiredPaymentsViewSet


router=routers.DefaultRouter()
router.register(r'expired-payments', ExpiredPaymentsViewSet)

urlpatterns=[]

urlpatterns += router.urls