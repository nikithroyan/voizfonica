from django.db import models

# Create your models here.


class prepaid_recharge(models.Model):
    plan_name = models.CharField(max_length=30)
    benefits = models.CharField(max_length=60)
    validity = models.CharField(max_length=60)
    price = models.IntegerField()
    def __str__(self):
        return self.plan_name






