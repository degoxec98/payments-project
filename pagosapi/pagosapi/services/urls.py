from django.urls import re_path
from rest_framework import routers
from .views import GetAllServiceView,ServiceViewSet


router=routers.DefaultRouter()
router.register(r'service', ServiceViewSet)

urlpatterns=[
    re_path(r'service',GetAllServiceView.as_view()),
]

urlpatterns += router.urls