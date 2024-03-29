from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

import cloudinary
from cloudinary.uploader import upload
from DB.models import *
from Orders.models import *




def registerPage(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            a = Profile(username = form.cleaned_data.get('username'), 
                first_name = form.cleaned_data.get('FirstName'), 
                last_name= form.cleaned_data.get('LastName'),
                email = form.cleaned_data.get('email'),
                Address = form.cleaned_data.get('Address'),
                Seller = form.cleaned_data.get('Seller'))
            a.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Account Created Successfully!')

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('Home')
        
        return render(request, 'Register.html', {'form': form, "Errors" : _Errors })
    elif request.method == "GET":
        if request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, 'You are already logged in idiot!')
            return redirect('Home')
        form = SignUpForm()
        return render(request, 'Register.html',{'form':form})



def logoutUser(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully logged out of the session!')
    return redirect('login')
def loginPage(request):
    context= {'User' : User}
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'Logged in Successfully!')
            return redirect('Home') 
        else:
            messages.add_message(request,messages.ERROR, 'Username Or Password Is Incorrect boi')
            return render (request,'Login.html', context)
    if request.user.is_authenticated:
            messages.add_message(request, messages.ERROR, 'You are already logged in idiot!')
            return redirect('Home')
    return render (request,'Login.html', context)

def Profiles(request, ProfileName):
    try:
        _Profile = Profile.objects.get(username = ProfileName)
    except:
        return render (request, 'ProfileNotFound.html')

    Context = {'Profile':_Profile}
    if _Profile.Seller == True:
        return render (request, 'Profile.html',Context)
    elif _Profile.Seller == False:
        return render (request, 'ProfileNotFound.html')

@login_required(login_url='/Login')
def Dashboard(request):
    username = request.user.username
    _Profile = Profile.objects.get(username = username)

    if _Profile.Seller == True:
        Product_D = Desktop.objects.filter(Dealer__username = username)
        Product_L = Laptop.objects.filter(Dealer__username = username)

        _Orders_P = Orders.objects.filter(Dealer__username = username, Status = "1")
        _Orders_D = Orders.objects.filter(Dealer__username = username, Status = "2")
        _Orders_C = Orders.objects.filter(Dealer__username = username, Status = "3")
        _Orders_R = Orders.objects.filter(Dealer__username = username, Status = "4")
        _Orders_RR = Orders.objects.filter(Dealer__username = username, Status = "5")

        Context = {'Profile': _Profile, 'Desk':Product_D, 'Lap':Product_L, 'OrdersP':_Orders_P, 'OrdersD':_Orders_D, 'OrdersC':_Orders_C, 'OrdersR':_Orders_R, 'OrdersRR': _Orders_RR}
        return render(request, 'Dashboard.html', Context)
    else:
        return render(request, 'NoDash.html')

def DeleteOrder(request,Prod):
    Obj = Orders.objects.get(Product_Name = Prod)
    Obj.delete()
    return redirect('Dashboard')
def DeleteObject(request,Cate,Prod):
    if Cate == "Desktops":
        Obj = Desktop.objects.get(Name = Prod)
    elif Cate == "Laptops":
        Obj = Laptop.objects.get(Name = Prod)
    Obj.delete()
    return redirect('Dashboard')

@login_required(login_url='/Login')
def CreateProduct(request):
    if request.method == "POST":
        data = request.POST.copy()
        Di = data.dict()
        try:
            Di['Image1']
            Image1 = 'https://gamer-zoned.herokuapp.com/uploads/image-available.jpg'
        except KeyError:
            _Image1 = cloudinary.uploader.upload(request.FILES['Image1'])
            Image1 = _Image1['url']
        try:
            Di['Image2']
            Image2 = 'https://gamer-zoned.herokuapp.com/uploads/image-available.jpg'
        except KeyError:
            _Image2 = cloudinary.uploader.upload(request.FILES['Image2'])
            Image2 = _Image2['url']
        try:
            Di['Image3']
            Image3 = 'https://gamer-zoned.herokuapp.com/uploads/image-available.jpg'
        except KeyError:
            _Image3 = cloudinary.uploader.upload(request.FILES['Image3'])
            Image3 = _Image3['url']
        try:
            Di['Image4']
            Image4 = 'https://gamer-zoned.herokuapp.com/uploads/image-available.jpg'
        except KeyError:
            _Image4 = cloudinary.uploader.upload(request.FILES['Image4'])
            Image4 = _Image4['url']
        try:
            Di['Image5']
            Image5 = 'https://gamer-zoned.herokuapp.com/uploads/image-available.jpg'
        except KeyError:
            _Image5 = cloudinary.uploader.upload(request.FILES['Image5'])
            Image5 = _Image5['url']
        if Di['Type'] == "1":
            instance = Desktop(str(request.user.username), Name = Di['Name'],Desc = Di['Desc'], Price = Di['Price'], Choice = Di['Type2'],Image1 = Image1,Image2 = Image2,Image3 = Image3,Image4 = Image4,Image5 = Image5, CPU = Di['CPU'], CPU_MODEL = Di['CpuModel'], RAM = Di['RAM'],RAM_SPEED = Di['RamSpeed'], GPU = Di['GPU'],GPU_Model = Di['GPUMODEL'], SSD = Di['SSD'], SSD_BRAND = Di['SSDBrand'], HDD = Di['HDD'], HDD_BRAND = Di['HDDBrand'], RefreshRate = Di['Refresh'], OS = Di['OS'], WARRANTY = Di['WARRANTY'])
            instance.save()
        if Di['Type'] == "2":
            instance = Laptop(str(request.user.username), Name = Di['Name'],Desc = Di['Desc'], Price = Di['Price'], Choice = Di['Type2'],Image1 = Image1,Image2 = Image2,Image3 = Image3,Image4 = Image4,Image5 = Image5, CPU = Di['CPU'], CPU_MODEL = Di['CpuModel'], RAM = Di['RAM'],RAM_SPEED = Di['RamSpeed'], GPU = Di['GPU'],GPU_Model = Di['GPUMODEL'], SSD = Di['SSD'], SSD_BRAND = Di['SSDBrand'], HDD = Di['HDD'], HDD_BRAND = Di['HDDBrand'], RefreshRate = Di['Refresh'], OS = Di['OS'], WARRANTY = Di['WARRANTY'])
            instance.save()
        return redirect('Dashboard')
    elif request.method == "GET":
        return render(request, 'Create.html')
@login_required(login_url='/Login')
def EditObject(request,Cate,Prod):
    if Cate == "Desktops":
        Obj = Desktop.objects.get(Name = Prod)
        Type = 'Desktops'
    elif Cate == "Laptops":
        Obj = Laptop.objects.get(Name = Prod)
        Type = 'Laptops'
    Set = {"Product":Obj, 'Type':Type }
    return render(request,'Edit.html',Set)

@login_required(login_url='/Login')
def MyCart(request):
    user = request.user.username
    Items = Carts.objects.filter(user = user, Ordered = False)
    Total = 0
    for i in Items:
        Total +=int(i.Price)

    Misc = {'Total': Total}
    Set = {'Items':Items, 'Misc':Misc}
    return render(request, 'Cart.html', Set)

@login_required(login_url='/Login')
def MyComments(request):
    user = request.user.username
    _Profile = Profile.objects.get(username = user)
    _Comments = Comments.objects.filter(User = _Profile)
    Di = {'Comments':_Comments}
    return render(request, 'Comments.html',Di)

@login_required(login_url='/Login')
def DeleteComment(request, Id):

    _Comments = Comments.objects.get(Id = Id)
    _Comments.delete()
    return redirect('Comments')
@login_required(login_url='/Login')
def Wishlist(request):
    _WishList = WishList.objects.filter(User = request.user)
    DIct = {'Wishlist':_WishList}
    return render(request, 'Wishlist.html', DIct)