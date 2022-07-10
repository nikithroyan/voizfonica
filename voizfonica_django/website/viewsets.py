from rest_framework import viewsets

from website import serializers
from website.models import prepaid_recharge


class websiteViewSet(viewsets.ModelViewSet):
    queryset = prepaid_recharge.objects.all()
    serializer_class=serializers.websiteSerializer

