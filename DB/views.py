from django.shortcuts import render,HttpResponse
from .models import *

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
    if str(Site) == "Desktops":
        Obj = Desktop.objects.get(Name = Prod)
    elif str(Site)  == "Laptops":
        Obj = Laptop.objects.get(Name = Prod)
    Set = {"Product":Obj, "Vars" : Vars}
    return render(request, 'Product.html', Set)
    