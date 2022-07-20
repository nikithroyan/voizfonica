from django.db import models

# Create your models here.


class prepaid_recharge(models.Model):
    id = models.IntegerField(primary_key=True)
    plan_name = models.CharField(max_length=50)
    benefits = models.CharField(max_length=150)
    validity = models.CharField(max_length=60)
    amount = models.IntegerField()
    def __str__(self):
        return self.id


class postpaid_recharge(models.Model):
    id = models.IntegerField(primary_key=True)
    plan_name = models.CharField(max_length=50)
    benefits = models.CharField(max_length=150)
    amount = models.IntegerField()
    def __str__(self):
        return self.id


class dongle_recharge(models.Model):
    id = models.IntegerField(primary_key=True)
    plan_name = models.CharField(max_length=50)
    benefits = models.CharField(max_length=150)
    validity = models.CharField(max_length=60)
    amount = models.IntegerField()
    def __str__(self):
        return self.id


class customer(models.Model):
    id = models.IntegerField(primary_key=True)
    connection_type = models.CharField(max_length=30)
    customer_name = models.CharField(max_length=70)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    aadhar = models.BigIntegerField()
    address = models.CharField(max_length=150)
    pin = models.IntegerField()

    def __str__(self):
        return self.id


class order(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    product_name = models.CharField(max_length=50)
    price = models.IntegerField()
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.id

class payment(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=60)
    amount = models.IntegerField()
    card_num = models.BigIntegerField()
    exp_month = models.IntegerField()
    exp_year = models.IntegerField()
    cvv = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.id

class query(models.Model):
    id = models.IntegerField(primary_key=True)
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=30)

    def __str__(self):
        return self.id
