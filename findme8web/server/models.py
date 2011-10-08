from django.db import models

# Create your models here.

class Account(models.Model):
    
    email = models.EmailField()
    
    accountname = models.CharField(max_length=200)
    
    
class DeviceLocation(models.Model):
    
    x_coordinate = models.CharField(max_length=50)
    
    y_coordinate = models.CharField(max_length=50)
    
    
