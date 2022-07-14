from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from website.models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class prepaidForm(forms.ModelForm):
    class Meta:
        model = prepaid_recharge
        fields = "__all__"

class postpaidForm(forms.ModelForm):
    class Meta:
        model = postpaid_recharge
        fields = "__all__"

class dongleForm(forms.ModelForm):
    class Meta:
        model = dongle_recharge
        fields = "__all__"


class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = "__all__"


class paymentForm(forms.ModelForm):
    class Meta:
        model = payment
        fields = "__all__"


class queryForm(forms.ModelForm):
    class Meta:
        model = query
        fields = "__all__"