from django.shortcuts import render,redirect # sayfaya yönlendirir
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    products = Card.objects.all().order_by("?")[0:3]
    productsg = Card.objects.get(id=2)
    productsf = Card.objects.filter(brand = "Iphone")
    
    context ={
        "products":products,
        "productsg":productsg,
        "productsf":productsf,
        


    }


    return render(request, 'index.html',context)

def Detail(request,id):
    products = Card.objects.get(id=id)
    comments = Comment.objects.filter(card=products)

    if request.method =="POST":
        name = request.POST["name"]
        title = request.POST["title"]
        text = request.POST["text"]

        comment = Comment(name=name,title=title,text=text,card=products)
        comment.save()
        return redirect("/detay/" + id + "/")

    context={
        "products":products,
        "comments":comments,
    }

    return render(request,'detail.html',context)


def allProduct(request, brandurl = "All"):
    if brandurl != "All":
        products = Card.objects.filter(brand__icontains = brandurl)
    else:
        products = Card.objects.all()

    context ={
        "products":products

    }

    return render(request,'allproduct.html',context)

#USER
def loginUser(requset):
    context ={}
    if requset.method == "POST":
        username = requset.POST["username"]
        password = requset.POST["password"]

        user = authenticate(username = username, password = password) #Kullanıcının olup olmadığını kontrol eder,  eğer yoksa değeri None'dır
        if user is not None:
            login(requset,user)
            return redirect('index')
        else:
            context.update({"hata":"Kullanıcı adı veya şifre yanlış!"})
    return render(requset,"users/login.html",context)

def logoutUser(requset):
    logout(requset)

    return redirect('loginUser')

def registerUser(request):
    context={}
    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=name,last_name=surname)
                user.save()
                return redirect('loginUser')
            else:
                context.update({"hata":"Kullanıcı adı daha önceden alınmış!"})
        
    return render(request,'users/register.html',context)