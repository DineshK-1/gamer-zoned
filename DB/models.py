from django.db import models
from django.apps import apps
from Accounts.models import Profile
from cloudinary.models import CloudinaryField

# Create your models here.

class Desktop(models.Model):

    Dealer = models.ForeignKey(Profile,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True,blank=True)
    Name = models.CharField(primary_key=True, max_length=40)
    Desc = models.TextField()
    Price = models.IntegerField()

    Category_List = [
        ("1", "Gaming"),
        ("2", "Workstation"),
        ("3", "Domestic"),
    ]
    Choice = models.CharField(max_length=1, choices=Category_List)

    Image1 = models.URLField(max_length = 200)
    Image2 = models.URLField(max_length = 200)
    Image3 = models.URLField(max_length = 200)
    Image4 = models.URLField(max_length = 200)
    Image5 = models.URLField(max_length = 200)
    # Sorting
    Category_List = [
        ("1", "Gaming"),
        ("2", "Workstation"),
        ("3", "Domestic"),
    ]
    CPU_CHOICES = [
        ("1", "Intel"),
        ("2", "AMD"),
    ]
    CPU = models.CharField(max_length=1, choices=CPU_CHOICES)
    CPU_MODEL = models.CharField(max_length=100)

    RAM_CHOICES = [
        ("1", "DDR3"),
        ("2", "DDR4"),
    ]
    RAM = models.CharField(max_length=1, choices=RAM_CHOICES)
    RAM_SPEED = models.CharField(max_length=100)

    GPU_SUB = [
        ("1", "Nvidia"),
        ("2", "AMD"),
    ]
    GPU = models.CharField(max_length=2, choices=GPU_SUB)
    GPU_Model = models.CharField(max_length = 100)

    SSD = models.BooleanField(blank=True, null=True)
    SSD_BRAND = models.CharField(max_length=100, null = True, blank = True)

    HDD_CHOICE = [
        ("1", "2 TB"),
        ("2", "1 TB")
    ]
    HDD = models.CharField(max_length=1, choices=HDD_CHOICE)
    HDD_BRAND = models.CharField(max_length=100)

    RefreshRate = models.CharField(max_length=10)

    OS = models.CharField(max_length=100)
    WARRANTY=models.CharField(max_length=100)
    def __str__(self):
        return str(self.Name)


class Laptop(models.Model):

    Dealer = models.ForeignKey(Profile,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    Name = models.CharField(primary_key=True, max_length=40)
    Desc = models.TextField()
    Price = models.IntegerField()

    Category_List = [
        ("1", "Gaming"),
        ("2", "Workstation"),
        ("3", "Domestic"),
    ]
    Choice = models.CharField(max_length=1, choices=Category_List)

    Image1 = models.URLField(max_length = 200)
    Image2 = models.URLField(max_length = 200)
    Image3 = models.URLField(max_length = 200)
    Image4 = models.URLField(max_length = 200)
    Image5 = models.URLField(max_length = 200)
    # Sorting
    Category_List = [
        ("1", "Gaming"),
        ("2", "Workstation"),
        ("3", "Domestic"),
    ]
    CPU_CHOICES = [
        ("1", "Intel"),
        ("2", "AMD"),
    ]
    CPU = models.CharField(max_length=1, choices=CPU_CHOICES)
    CPU_MODEL = models.CharField(max_length=100)

    RAM_CHOICES = [
        ("1", "DDR3"),
        ("2", "DDR4"),
    ]
    RAM = models.CharField(max_length=1, choices=RAM_CHOICES)
    RAM_SPEED = models.CharField(max_length=100)

    GPU_SUB = [
        ("1", "Nvidia"),
        ("2", "AMD"),
    ]
    GPU = models.CharField(max_length=2, choices=GPU_SUB)
    GPU_Model = models.CharField(max_length = 100)

    SSD = models.BooleanField(blank=True, null=True)
    SSD_BRAND = models.CharField(max_length=100)

    HDD_CHOICE = [
        ("1", "2 TB"),
        ("2", "1 TB")
    ]
    HDD = models.CharField(max_length=1, choices=HDD_CHOICE)
    HDD_BRAND = models.CharField(max_length=100)
    

    RefreshRate = models.CharField(max_length=10)

    OS = models.CharField(max_length=100)
    WARRANTY=models.CharField(max_length=100)

    def __str__(self):
        return self.Name + " BY " + str(self.Dealer)

class Comments(models.Model):
    User = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Comment = models.CharField(max_length = 150)
    Product = models.CharField(max_length = 150)
    Date = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    Upvotes = models.IntegerField()
    Downvotes = models.IntegerField()

class Review(models.Model):
    User = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Product = models.CharField(max_length = 200)
    Rating = models.IntegerField()
