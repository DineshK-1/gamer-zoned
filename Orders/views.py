from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import Carts,Orders
from datetime import datetime
from Accounts.models import Profile
from DB.models import Desktop,Laptop
from .utils import unique_order_id_generator

# Create your views here.
def SubmitItem(request):
    if request.method == 'POST':
        data = request.POST.copy()
        Di = data.dict()
        instance = Carts(user_id = request.user.username,Item = Di['Name'], Price = Di['Price'])
        instance.save()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
    elif request.method == 'GET':
        return render(request, 'PageNotFound.html')

def Checkout(request):
    user = request.user.username
    Products = Carts.objects.filter(user = user, Ordered = False)

    if not Products:
        return render(request, 'PageNotFound.html')

    ProductsList = []
    for i in Products:
        try:
            Desk = Desktop.objects.get(Name = i.Item)
            Dealer = str(Desk.Dealer)
        except:
            Lap = Laptop.objects.get(Name = i.Item)
            Dealer = str(Lap.Dealer)
        Order_id = unique_order_id_generator()
        instance = Orders(User = Profile.objects.get(username = user), Dealer = Profile.objects.get(username = Dealer), Product_Name = i.Item, Price = i.Price, Order_id = Order_id)
        instance.save()
        i.Ordered = True
        i.Date_Ordered = datetime.now()
        i.save()
        ProductsList.append(str(i.Item))

    Dict = {'Products': ProductsList}
    print(Dict)
    return render(request, 'Sucess.html',Dict)
def CancelOrder(request, OrderId):
    Order = Orders.objects.get(Order_id = OrderId)
    Order.Status = "3"
    Order.save()
    return redirect('Dashboard')
def ConfirmOrder(request, OrderId):
    Order = Orders.objects.get(Order_id = OrderId)
    Order.Status = "2"
    Order.save()
    return redirect('Dashboard')

def OrderPage(request):
    OrdersP = Orders.objects.filter(User = request.user.username, Status = "1")
    OrdersD = Orders.objects.filter(User = request.user.username, Status = "2")
    OrdersC = Orders.objects.filter(User = request.user.username, Status = "3")
    OrdersR = Orders.objects.filter(User = request.user.username, Status = "4")
    OrdersRR = Orders.objects.filter(User = request.user.username, Status = "5")
    Context = {'OrdersP':OrdersP, 'OrdersD':OrdersD, 'OrdersC':OrdersC, 'OrdersR':OrdersR, 'OrdersRR':OrdersRR}

    return render(request, 'Orders.html', Context)

def Refund(request,OrderId):
    Order = Orders.objects.get(Order_id = OrderId)
    Order.Status = "5"
    Order.save()
    return redirect('Orders')
def RefundDash(request, OrderId):
    Order = Orders.objects.get(Order_id = OrderId)
    Order.Status = "4"
    Order.save()
    return redirect('Dashboard')