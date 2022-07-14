from rest_framework import serializers
from website.models import prepaid_recharge, postpaid_recharge, dongle_recharge, customer, order, payment, query


class prepaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = prepaid_recharge
        fields = '__all__'

class postpaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = postpaid_recharge
        fields = '__all__'

class dongleSerializer(serializers.ModelSerializer):
    class Meta:
        model = dongle_recharge
        fields = '__all__'


class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'


class orderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = '__all__'


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'


class querySerializer(serializers.ModelSerializer):
    class Meta:
        model = query
        fields = '__all__'''