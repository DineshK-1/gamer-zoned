from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from DB.views import *
from Accounts.views import *
from Orders.views import *

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+[
    path('admin/', admin.site.urls),
    path('CreateProduct/',CreateProduct,name='Create'),
    path('SubmitItem/',SubmitItem),
    path('AddComment/',AddComment),
    path('SubmitRating/', SubmitRating, name= "Rating"),
    path('MyCart/',MyCart,name="Cart"),
    path('Wishlist/',Wishlist,name="Wishlist"),
    path('AddWish/',AddWish),
    path('DelWish/<str:Id>',DelWish),
    path('MyComments/',MyComments,name="Comments"),
    path('DeleteComment/<str:Id>',DeleteComment),
    path('Checkout/',Checkout,name = 'Checkout'),
    path('MyOrders/',OrderPage,name = 'Orders'),
    path('MyOrders/<str:OrderId>/Refund',Refund,name = 'Orders'),
    path('Profiles/<str:ProfileName>',Profiles),
    path('Dashboard', Dashboard, name = 'Dashboard'),
    path('Dashboard/<str:Cate>/<str:Prod>/Edit', EditObject),
    path('Dashboard/<str:OrderId>/Cancel', CancelOrder),
    path('Dashboard/<str:OrderId>/Confirm', ConfirmOrder),
    path('Dashboard/<str:Cate>/<str:Prod>/Delete', DeleteObject),
    path('Dashboard/<str:OrderId>/Refund',RefundDash),
    path('',Home, name = "Home"),
    path('<Site>/<str:Cate>', GamingD),
    path('<Site>/<str:Cate>/<str:Prod>', ProductGD),
    path('<Site>/<str:Cate>/<str:Prod>', ProductGD),
    path('Login', loginPage, name= "login"),
    path('Register', registerPage, name = "register"),
    path('Logout', logoutUser, name = "logout"),
]
