from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps

class Profile(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    Seller = models.BooleanField(blank=True,null=True)
    Address = models.TextField()
    def __str__(self):
        return self.username

class WishList(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length = 100)
    Class_Choice=[('1', 'Desktop'),('2', 'Laptop')]
    Class = models.CharField(max_length = 1, choices = Class_Choice)
    SubClass_Choice=[('1', 'Gaming'),('2', 'Workstation'),('3', 'Domestic')]
    SubClass = models.CharField(max_length = 1, choices = SubClass_Choice)
    
