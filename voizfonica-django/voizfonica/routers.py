from rest_framework import routers
# from website.models import prepaid_recharge

from website.viewsets import prepaidViewSet, postpaidViewSet, dongleViewSet, customerViewSet, orderViewSet, paymentViewSet, queryViewSet

router = routers.DefaultRouter()
router.register('prepaid_recharge', prepaidViewSet)
router.register('postpaid_recharge', postpaidViewSet)
router.register('dongle_recharge', dongleViewSet)
router.register('customer', customerViewSet)
router.register('order', orderViewSet)
router.register('payment', paymentViewSet)
router.register('query', queryViewSet)



