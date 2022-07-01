
from django.db import models
from django.db.models.fields import *

# Create your models here.
class Donate(models.Model):
    name = models.CharField(max_length=64)
    Amount = models.IntegerField()
    
class DonateDetail(models.Model):
    name = models.CharField(max_length=64)
    Amount = models.IntegerField()
    