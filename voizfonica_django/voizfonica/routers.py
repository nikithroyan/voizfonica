from rest_framework import routers
from website.models import prepaid_recharge

from website.viewsets import websiteViewSet

router = routers.DefaultRouter()
router.register('prepaid_recharge', websiteViewSet)
