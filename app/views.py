from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import createuser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import card,product_details,cart_model

def admn(request):
    data = card.objects.order_by('?')[:4]
    return render(request,'adminp.html',{"data":data})

def register(request):
    if request.method=='POST':
        name=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1==password2:
            user=User.objects.create_user(username=name,email=email,password=password1)
            user.save()
            messages.success(request,"your Registration is success")
            return redirect('login')
        else:
            messages.warning(request,"password is not same !!!! ")
            return redirect('register')
    else:
        form = createuser()
        return render(request,'register.html',{'form':form})

@login_required
def profile(request):
    return render(request,"profile.html")

def trys(request):
    return render(request,"try.html")

@login_required
def product(request,model):
    datas = product_details.objects.get(model=model)
    data = card.objects.get(model=model)
    return render(request,"product.html",{'data':data,'datas':datas})
@login_required
def moblie(request,category):
    data = card.objects.filter(category=category).values()
    tag = category
    return render(request,"moblie.html",{"data":data,'tag':tag})

@login_required
def home(request):
    data = card.objects.all()
    return render(request,'home.html',{'data':data})

@login_required
def addcart(request,id):
    data = card.objects.get(id=id)
    datas = cart_model.objects.all()
    dt = datas.exists()
    if dt:
        if all(d1.model != data.model for d1 in datas):
            carts = cart_model()
            img = data.img
            modl = data.model
            price = data.price
            brand = data.brand
            info = data.info
            cat = data.category
            carts.img = img
            carts.model = modl
            carts.info = info
            carts.price = price
            carts.brand = brand
            carts.category = cat
            carts.save()
            return redirect('cart')
        else:
            return redirect('cart')
    else:
        carts = cart_model()
        img = data.img
        modl = data.model
        price = data.price
        brand = data.brand
        info = data.info
        cat = data.category
        carts.img = img
        carts.model = modl
        carts.info = info
        carts.price = price
        carts.brand = brand
        carts.category = cat
        carts.save()
        return redirect('cart')


@login_required
def cart(request):
    data = cart_model.objects.all()
    return render(request,'cart.html',{'data':data})

@login_required
def remove_cart(request,id):
    data = cart_model.objects.get(id=id)
    data.delete()
    return redirect('cart')