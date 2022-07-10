from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from website.models import prepaid_recharge


class RechargeForm(forms.ModelForm):
    class Meta:
        model = prepaid_recharge
        fields = "__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
