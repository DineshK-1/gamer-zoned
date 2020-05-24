from django.db import models
from DB.models import Desktop,Laptop
from Accounts.models import Profile
from django.db.models.signals import pre_save

# Create your models here.

class Carts(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    Date = models.DateTimeField(auto_now_add=True,blank=True)
    Item = models.CharField(max_length=100)
    Price = models.IntegerField()
    Ordered = models.BooleanField(default=False)
    Date_Ordered = models.DateTimeField(blank=True,null = True)

class Orders(models.Model):
    User = models.ForeignKey(Profile,on_delete=models.DO_NOTHING, related_name="User")
    Dealer = models.ForeignKey(Profile,on_delete=models.DO_NOTHING, related_name="Dealer")

    Product_Name = models.CharField(max_length=200)
    Price = models.IntegerField()
    Timestamp = models.DateTimeField(auto_now_add=True)
    
    Order_id = models.CharField(max_length = 120, blank = True, null =True)
    
    ORDER_STATUS_CHOICES= (
    ('1', 'Not Yet Shipped'),
    ('2', 'Shipped'),
    ('3', 'Cancelled'),
    ('4', 'Refunded'),
    ('5', 'Refund Requested')
    )

    Status = models.CharField(max_length = 1, choices = ORDER_STATUS_CHOICES, default = '1')

    def __str__(self):
        return str(self.Order_id) + ' By ' +self.User.username + ' at ' + str(self.Timestamp)