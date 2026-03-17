from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter = models.BooleanField(default=False)
    email_address = models.CharField(max_length=100, blank=True, default="")
    account = models.FloatField(blank=True, null=True)