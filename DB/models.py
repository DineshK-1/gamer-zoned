from django.db import models
from django.apps import apps
from Accounts.models import Profile

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

    Image1 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')
    Image2 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')
    Image3 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')
    Image4 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')
    Image5 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')

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

    Image1 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')
    Image2 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')
    Image3 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')
    Image4 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')
    Image5 = models.ImageField(
        upload_to='uploads/', default='uploads/image-available.jpg')

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
