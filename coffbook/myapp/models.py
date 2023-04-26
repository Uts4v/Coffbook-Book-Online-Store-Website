from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField (max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=120, primary_key=True, null=False, default="")    

class Users(models.Model):
    username=models.CharField(max_length=120, null=True)
    email=models.CharField(max_length=120, primary_key=True, unique=True, default="NULL")
    password=models.CharField(max_length=120, null=True)
    
class Home(models.Model):
    name = models.CharField (max_length=120, null=True)
    email = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=120, primary_key=True, null=False, default="")       

class Bought(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField (max_length=120, null=True)
    bookname = models.CharField(max_length=120, null=True)
    price = models.CharField(max_length=120, null=0)


    
