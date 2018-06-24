from django.conf.urls import include, url
from rest_framework import routers
from general.views import *


router = routers.SimpleRouter()
router.register(r'general_info', GeneralViewSet, base_name="General")

# urlpatterns = [
#     url(r'^forgot-password/$', ForgotPasswordFormView.as_view()),
# ]

# urlpatterns += router.urls

urlpatterns = router.urls