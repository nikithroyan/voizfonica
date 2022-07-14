"""voizfonica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
'''from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
#    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('home', views.home, name="home"),
]'''

from django.contrib import admin
from django.urls import path

from voizfonica.routers import router
from website import views

from django.urls import include, path
from rest_framework import routers

from website.views import prepaid_rechargelist
from website.viewsets import prepaidViewSet, postpaidViewSet, dongleViewSet, customerViewSet, orderViewSet, paymentViewSet, queryViewSet

router = routers.DefaultRouter()
router.register('list1', prepaidViewSet, basename='list1')
router.register('list2', postpaidViewSet, basename='list2')
router.register('list3', dongleViewSet, basename='list3')
router.register('list4', customerViewSet, basename='list4')
router.register('list5', orderViewSet, basename='list5')
router.register('list6', paymentViewSet, basename='list6')
router.register('list7', queryViewSet, basename='list7')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('home', views.home, name="home"),
    path('Admin', views.Admin, name="Admin"),
    path('display_prepaid', views.display_prepaid, name="display_prepaid"),
    path('display_postpaid', views.display_postpaid, name="display_postpaid"),
    path('display_dongle', views.display_dongle, name="display_dongle"),
    path('display_customer', views.display_customer, name="display_customer"),
    path('display_payment', views.display_payment, name="display_payment"),
    path('display_query', views.display_query, name="display_query"),
    path('new_prepaid', views.new_prepaid, name="new_prepaid"),
    path('new_postpaid', views.new_postpaid, name="new_postpaid"),
    path('new_dongle', views.new_dongle, name="new_dongle"),
    path('new_customer', views.new_customer, name="new_customer"),
    path('update_prepaid/<int:id>', views.update_prepaid, name="update_prepaid"),
    path('update_postpaid/<int:id>', views.update_postpaid, name="update_postpaid"),
    path('update_dongle/<int:id>', views.update_dongle, name="update_dongle"),
    path('update_customer/<int:id>', views.update_customer, name="update_customer"),
    path('update_query/<int:id>', views.update_query, name="update_query"),
    path('delete_prepaid/<int:id>', views.delete_prepaid, name="delete_prepaid"),
    path('delete_postpaid/<int:id>', views.delete_postpaid, name="delete_postpaid"),
    path('delete_dongle/<int:id>', views.delete_dongle, name="delete_dongle"),
    path('delete_customer/<int:id>', views.delete_customer, name="delete_customer"),
    path('delete_query/<int:id>', views.delete_query, name="delete_query"),

    #    path('list/',views.get,name='get')
]

