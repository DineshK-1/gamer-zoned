from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from .utils import unique_order_id_generator
from Accounts.models import WishList
# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def GamingD(request, Site,Cate):
    Vars = {"Site":Site, "Cate":Cate}
    if Site == "Desktops":
        if Cate == "Gaming":
            Set = Desktop.objects.filter(Choice = "1")
            if request.method == "GET":
                Dict = {"Set":Set, "Vars" : Vars}
                return render(request, 'ProductsGD.html',Dict)
                
            elif request.method == "POST":
                data = request.POST.copy()
                Di = data.dict()
                L=[]
                FilteredSet=Set
                for i in Di:
                    L.append(i)
                for j in L:
                    if j == 'CPU':
                        Value = Di["CPU"]
                        FilteredSet = FilteredSet.filter(CPU = Value)
                    if j == 'RAM':
                        Value = Di["RAM"]
                        FilteredSet = FilteredSet.filter(RAM = Value)
                    if j == 'GPU':
                        Value = Di["GPU"]
                        FilteredSet = FilteredSet.filter(GPU = Value)
                    if j == 'SSD':
                        Value = Di['SSD']
                        if Value == '1':
                            Value = True
                        else:
                            Value = False
                        FilteredSet = FilteredSet.filter(SSD = Value)
                    if j == 'HDD':
                        Value = Di['HDD']
                        FilteredSet = FilteredSet.filter(HDD = Value)
                    
                FilteredDict = {"Set":FilteredSet,'Checks':Di, "Vars" : Vars}

                return render(request, 'ProductsGD.html',FilteredDict)
        
        if Cate == "Workstation":
            Set = Desktop.objects.filter(Choice = "2")
        
            if request.method == "GET":
                Dict = {"Set":Set, "Vars" : Vars}
                return render(request, 'ProductsGD.html',Dict)
                
            elif request.method == "POST":
                data = request.POST.copy()
                Di = data.dict()
                L=[]
                FilteredSet=Set
                for i in Di:
                    L.append(i)
                for j in L:
                    if j == 'CPU':
                        Value = Di["CPU"]
                        FilteredSet = FilteredSet.filter(CPU = Value)
                    if j == 'RAM':
                        Value = Di["RAM"]
                        FilteredSet = FilteredSet.filter(RAM = Value)
                    if j == 'GPU':
                        Value = Di["GPU"]
                        FilteredSet = FilteredSet.filter(GPU = Value)
                    if j == 'SSD':
                        Value = Di['SSD']
                        if Value == '1':
                            Value = True
                        else:
                            Value = False
                        FilteredSet = FilteredSet.filter(SSD = Value)
                    if j == 'HDD':
                        Value = Di['HDD']
                        FilteredSet = FilteredSet.filter(HDD = Value)
                FilteredDict = {"Set":FilteredSet,'Checks':Di, "Vars" : Vars}

                return render(request, 'ProductsGD.html',FilteredDict)
        
        if Cate == "Domestic":
            Set = Desktop.objects.filter(Choice = "3")

            if request.method == "GET":
                Dict = {"Set":Set, "Vars" : Vars}
                
                return render(request, 'ProductsGD.html',Dict)
                
            elif request.method == "POST":
                data = request.POST.copy()
                Di = data.dict()
                L=[]
                FilteredSet=Set
                for i in Di:
                    L.append(i)
                for j in L:
                    if j == 'CPU':
                        Value = Di["CPU"]
                        FilteredSet = FilteredSet.filter(CPU = Value)
                    if j == 'RAM':
                        Value = Di["RAM"]
                        FilteredSet = FilteredSet.filter(RAM = Value)
                    if j == 'GPU':
                        Value = Di["GPU"]
                        FilteredSet = FilteredSet.filter(GPU = Value)
                    if j == 'SSD':
                        Value = Di['SSD']
                        if Value == '1':
                            Value = True
                        else:
                            Value = False
                        FilteredSet = FilteredSet.filter(SSD = Value)
                    if j == 'HDD':
                        Value = Di['HDD']
                        FilteredSet = FilteredSet.filter(HDD = Value)  
                FilteredDict = {"Set":FilteredSet,'Checks':Di, "Vars" : Vars}

                return render(request, 'ProductsGD.html',FilteredDict)

    elif Site == "Laptops":
        if Cate == "Gaming":
            Set = Laptop.objects.filter(Choice = "1")
        
            if request.method == "GET":
                Dict = {"Set":Set, "Vars" : Vars}
                return render(request, 'ProductsGL.html',Dict)
                
            elif request.method == "POST":
                data = request.POST.copy()
                Di = data.dict()
                L=[]
                FilteredSet=Set
                for i in Di:
                    L.append(i)
                for j in L:
                    if j == 'CPU':
                        Value = Di["CPU"]
                        FilteredSet = FilteredSet.filter(CPU = Value)
                    if j == 'RAM':
                        Value = Di["RAM"]
                        FilteredSet = FilteredSet.filter(RAM = Value)
                    if j == 'GPU':
                        Value = Di["GPU"]
                        FilteredSet = FilteredSet.filter(GPU = Value)
                    if j == 'SSD':
                        Value = Di['SSD']
                        if Value == '1':
                            Value = True
                        else:
                            Value = False
                        FilteredSet = FilteredSet.filter(SSD = Value)
                    if j == 'HDD':
                        Value = Di['HDD']
                        FilteredSet = FilteredSet.filter(HDD = Value)
                        
                FilteredDict = {"Set":FilteredSet,'Checks':Di, "Vars" : Vars}

                return render(request, 'ProductsGL.html',FilteredDict)
        
        if Cate == "Domestic":
            Set = Laptop.objects.filter(Choice = "2")
        
            if request.method == "GET":
                Dict = {"Set":Set, "Vars" : Vars}
                return render(request, 'ProductsGL.html',Dict)
                
            elif request.method == "POST":
                data = request.POST.copy()
                Di = data.dict()
                L=[]
                FilteredSet=Set
                for i in Di:
                    L.append(i)
                    
                for j in L:
                    if j == 'CPU':
                        Value = Di["CPU"]
                        FilteredSet = FilteredSet.filter(CPU = Value)
                    if j == 'RAM':
                        Value = Di["RAM"]
                        FilteredSet = FilteredSet.filter(RAM = Value)
                    if j == 'GPU':
                        Value = Di["GPU"]
                        FilteredSet = FilteredSet.filter(GPU = Value)
                    if j == 'SSD':
                        Value = Di['SSD']
                        if Value == '1':
                            Value = True
                        else:
                            Value = False
                        FilteredSet = FilteredSet.filter(SSD = Value)
                    if j == 'HDD':
                        Value = Di['HDD']
                        FilteredSet = FilteredSet.filter(HDD = Value)      
                FilteredDict = {"Set":FilteredSet,'Checks':Di, "Vars" : Vars}

                return render(request, 'ProductsGL.html',FilteredDict)

        


def ProductGD(request,Site, Cate, Prod):
    Obj = None
    Vars = {"Site":Site, "Cate":Cate, "Prod" : Prod}
    if Cate == "Gaming":
        _Choice = '1'
    elif Cate == 'Workstation':
        _Choice = '2'
    elif Cate == "Domestic":
        _Choice = '3'
    if str(Site) == "Desktops":
        Obj = Desktop.objects.get(Name = Prod)
        Recommendations = Desktop.objects.filter(Choice = _Choice)
    elif str(Site)  == "Laptops":
        Obj = Laptop.objects.get(Name = Prod)
        Recommendations = Laptop.objects.filter(Choice = _Choice)
    Commentz = Comments.objects.filter(Product = Prod)

    Set = {"Product":Obj, "Vars" : Vars, "Comments":Commentz, "Recommendation": Recommendations}
    return render(request, 'Product.html', Set)

@login_required(login_url='/Login')
def AddComment(request):
    if request.method == 'POST':
        User = request.user.username
        _Profile = Profile.objects.get(username = User)
        data = request.POST.copy()
        Di = data.dict()
        Id = unique_order_id_generator()
        Comment = Di['Comment']
        Product = Di['Product']

        instance = Comments(Id = Id,User = _Profile, Comment = Comment, Product = Product, Upvotes = 0, Downvotes= 0)
        instance.save()

        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    elif request.method == 'GET':
        return render(request, 'PageNotFound.html')

def SubmitRating(request):
    pass
def AddWish(request):
    if request.method == "POST":
        Data = request.POST
        _Wish = WishList(User = request.user, Class = Data["Class"],SubClass = Data["SubClass"])
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    else:
        return render(request, 'PageNotFound.html')
def DelWish(request,id):
    if request.method == "POST":
        Data = request.POST
        _Wish = WishList.objects.get(id = id)
        _Wish.delete()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    else:
        return render(request, 'PageNotFound.html')