from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *

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
                if user.is_superuser:
                    return redirect('/Admin')
                # login(request)
                else:
                    return redirect('/home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def Admin(request):
    return render(request, 'admin.html')

def display_prepaid(request):
    records = prepaid_recharge.objects.all()
    return render(request, 'prepaid.html', {'records': records})

def new_prepaid(request):
    if request.method == 'POST':
        form = prepaidForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/display_prepaid')
            except:
                pass
    else:
        form = prepaidForm()
    return render(request, 'new.html', {'form': form})


def update_prepaid(request, id):
    obj = get_object_or_404(prepaid_recharge, id=id)
    form = prepaidForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/display_prepaid')
    return render(request, 'update.html', {'form': form})


def delete_prepaid(request, id):
    data = prepaid_recharge.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('/display_prepaid')
    return render(request, 'delete.html')


def display_postpaid(request):
    records = postpaid_recharge.objects.all()
    return render(request, 'postpaid.html', {'records': records})

def new_postpaid(request):
    if request.method == 'POST':
        form = postpaidForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/display_postpaid')
            except:
                pass
    else:
        form = postpaidForm()
    return render(request, 'new.html', {'form': form})


def update_postpaid(request, id):
    obj = get_object_or_404(postpaid_recharge, id=id)
    form = postpaidForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/display_postpaid')
    return render(request, 'update.html', {'form': form})


def delete_postpaid(request, id):
    data = postpaid_recharge.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('/display_postpaid')
    return render(request, 'delete.html')


def display_dongle(request):
    records = dongle_recharge.objects.all()
    return render(request, 'dongle.html', {'records': records})


def new_dongle(request):
    if request.method == 'POST':
        form = dongleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/display_dongle')
            except:
                pass
    else:
        form = dongleForm()
    return render(request, 'new.html', {'form': form})


def update_dongle(request, id):
    obj = get_object_or_404(dongle_recharge, id=id)
    form = dongleForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/display_dongle')
    return render(request, 'update.html', {'form': form})


def delete_dongle(request, id):
    data = dongle_recharge.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('/display_dongle')
    return render(request, 'delete.html')


def display_customer(request):
    records = customer.objects.all()
    return render(request, 'customer.html', {'records': records})


def new_customer(request):
    if request.method == 'POST':
        form = customerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/display_customer')
            except:
                pass
    else:
        form = customerForm()
    return render(request, 'new.html', {'form': form})


def update_customer(request, id):
    obj = get_object_or_404(customer, id=id)
    form = customerForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/display_customer')
    return render(request, 'update.html', {'form': form})


def delete_customer(request, id):
    data = customer.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('/display_customer')
    return render(request, 'delete.html')


def display_query(request):
    records = query.objects.all()
    return render(request, 'query.html', {'records': records})


def update_query(request, id):
    obj = get_object_or_404(query, id=id)
    form = queryForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/display_query')
    return render(request, 'update.html', {'form': form})


def delete_query(request, id):
    data = query.objects.get(id=id)
    if request.method == 'POST':
        data.delete()
        return redirect('/display_query')
    return render(request, 'delete.html')


def display_payment(request):
    records = payment.objects.all()
    return render(request, 'payment.html', {'records': records})


def username1(request):
    mobile = request.POST.get('mobile1')
    request.session['us1'] = mobile
    return render(request, 'username1.html')


def invoicebill(request):
    us = request.session['us1']
    mobile = us
    obj = customer.objects.get(mobile=mobile)
    id = obj.id
    plan = payment.objects.get(id=id)
    return render(request, 'invoicebill.html', {'plan': plan, 'obj': obj})


def logout(request):
    # logout(request)
    return redirect('/')


class prepaid_rechargelist(APIView):
    def get(self, request):
        queryset = prepaid_recharge.objects.all()
        obj = prepaidSerializer(queryset, many=True)
        return Response(obj.data)


class postpaid_rechargelist(APIView):
    def get(self, request):
        queryset = postpaid_recharge.objects.all()
        obj = postpaidSerializer(queryset, many=True)
        return Response(obj.data)

class dongle_rechargelist(APIView):
    def get(self, request):
        queryset = dongle_recharge.objects.all()
        obj = dongleSerializer(queryset, many=True)
        return Response(obj.data)


class customerlist(APIView):
    def get(self, request):
        queryset = customer.objects.all()
        obj = customerSerializer(queryset, many=True)
        return Response(obj.data)


class orderlist(APIView):
    def get(self, request):
        queryset = order.objects.all()
        obj = orderSerializer(queryset, many=True)
        return Response(obj.data)


class paymentlist(APIView):
    def get(self, request):
        queryset = payment.objects.all()
        obj = paymentSerializer(queryset, many=True)
        return Response(obj.data)


class querylist(APIView):
    def get(self, request):
        queryset = query.objects.all()
        obj = querySerializer(queryset, many=True)
        return Response(obj.data)

def home(request):
    return render(request, 'home.html')
