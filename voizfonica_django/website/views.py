from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
from .forms import CreateUserForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import websiteSerializer



# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('/')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                # login(request)
                return redirect('/home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logout(request):
    # logout(request)
    return redirect('/')

class prepaid_rechargelist(APIView):
    def get(self, request):
        queryset = prepaid_recharge.objects.all()
        obj = websiteSerializer(queryset, many=True)
        return Response(obj.data)

def home(request):
    return render(request, 'home.html')
