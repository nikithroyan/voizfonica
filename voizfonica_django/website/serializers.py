from rest_framework import serializers
from website.models import prepaid_recharge


class websiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = prepaid_recharge
        fields = '__all__'
