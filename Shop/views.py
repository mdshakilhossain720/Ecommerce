from django.shortcuts import render
from .models import Product
from django .views import View
from . forms import CustomRegestionForm
from django.contrib import messages


# Create your views here.
class ProductView(View):
     def get(self,request):
       
       gentspant=Product.objects.filter( categroy='Gp')
       borkhar=Product.objects.filter( categroy='Bc')
       babyfashion=Product.objects.filter( categroy='BF')
       return render(request, 'Shop/home.html',{'gentspant': gentspant,'borkhar':borkhar,'babyfashion':babyfashion})

class ProductDetailsView(View):
     def get(self,request,pk):
        products=Product.objects.get(pk=pk)
        return render(request, 'Shop/productdetail.html',{'products':products})

def add_to_cart(request):
 return render(request, 'Shop/addtocart.html')

def buy_now(request):
 return render(request, 'Shop/buynow.html')

def profile(request):
 return render(request, 'Shop/profile.html')

def address(request):
 return render(request, 'Shop/address.html')

def orders(request):
 return render(request, 'Shop/orders.html')

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request,data = None):
    if data == None:
         lehengas=Product.objects.filter(categroy='L')
    elif data =='lubnan' or data == 'infinity':
         lehengas=Product.objects.filter(categroy='L').filter(brand=data)
    elif data == 'above':
         lehengas=Product.objects.filter(categroy='L').filter(discount_gt=2000)
    elif data == 'blow':
         lehengas=Product.objects.filter(categroy='L').filter(discount_lt=2000)
       
       
    return render(request, 'Shop/lehenga.html',{'lehengas':lehengas})

def login(request):
     return render(request, 'Shop/login.html')

class CustomerRegestionView(View):
     def get (self,request):
       form=CustomRegestionForm()
       return render(request, 'Shop/customerregistration.html',{'form':form})
     
     def post(self,request):
        form=CustomRegestionForm(request.POST)
        if form.is_vaild():
           messages.success(request, 'Congrations Regestion done')
           form.save()
        return render(request, 'Shop/customerregistration.html',{'form':form})
           

def checkout(request):
 return render(request, 'Shop/checkout.html')
