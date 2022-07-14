from rest_framework import viewsets

from website import serializers
from website.models import prepaid_recharge, postpaid_recharge, dongle_recharge, customer, order, payment, query


class prepaidViewSet(viewsets.ModelViewSet):
    queryset = prepaid_recharge.objects.all()
    serializer_class=serializers.prepaidSerializer


class postpaidViewSet(viewsets.ModelViewSet):
    queryset = postpaid_recharge.objects.all()
    serializer_class=serializers.postpaidSerializer


class dongleViewSet(viewsets.ModelViewSet):
    queryset = dongle_recharge.objects.all()
    serializer_class=serializers.dongleSerializer


class customerViewSet(viewsets.ModelViewSet):
    queryset = customer.objects.all()
    serializer_class=serializers.customerSerializer


class orderViewSet(viewsets.ModelViewSet):
    queryset = order.objects.all()
    serializer_class=serializers.orderSerializer


class paymentViewSet(viewsets.ModelViewSet):
    queryset = payment.objects.all()
    serializer_class=serializers.paymentSerializer


class queryViewSet(viewsets.ModelViewSet):
    queryset = query.objects.all()
    serializer_class=serializers.querySerializer

