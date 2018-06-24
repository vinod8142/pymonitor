from django.conf.urls import include, url
from rest_framework import routers
from performance.views import *


router = routers.SimpleRouter()
router.register(r'performance_info', PerformanceViewSet, base_name="Performance")

urlpatterns = router.urls