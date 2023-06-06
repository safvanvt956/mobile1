from django.shortcuts import render,redirect
from . models import Product,Order,OrderItem
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.cart import Cart

# Create your views here.
def index(request):
    context = {
        'hello' : Product.objects.all()
    }

    return render(request,"web/index.html",context)


def login1(request):
    if request.method=="POST":
        username=request.POST.get('user_1')
        password=request.POST.get('pass_1')

        user = authenticate(username=username,password=password)
        if user is not None:

            login(request,user)
            return redirect('index')
        else:
            messages.warning(request,'invalid details')
            return redirect('login')
        

    return render(request,'web/account/login.html')


def signup1(request):
    if request.method=="POST":
        Username=request.POST.get('name_1')
        FirstName=request.POST.get('first_1')
        LastName=request.POST.get('last_1')
        Email=request.POST.get('email_1')
        Password=request.POST.get('pa_1')
        ConfirmPassword=request.POST.get('cp_1')

        if Password==ConfirmPassword:
            customer=User.objects.create_user(Username,Email,Password)
            customer.first_name=FirstName
            customer.last_name=LastName
            customer.save()
            return redirect('login')
    return render(request,'web/account/signup.html')   


def signout1(request):
     return render(request,'web/account/login.html')



def about(request):
     return render(request,'web/folder/about.html')

def service(request):
     return render(request,'web/folder/service.html')

def product(request):
     return render(request,'web/folder/product.html')

def price(request):
     return render(request,'web/folder/price.html')

def team(request):
     return render(request,'web/folder/team.html')

def contact(request):
     return render(request,'web/folder/contact.html')

def testimonial(request):
     return render(request,'web/folder/testimonial.html')

def blog(request):
     return render(request,'web/folder/blog.html')

def detail(request):
     return render(request,'web/folder/detail.html')






@login_required(login_url="login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'web/cart/cart.html')





@login_required(login_url="login")
def checkout(request):
    return render(request, 'web/checkout.html')


@login_required(login_url="login")
def right(request):
    return render(request, 'web/right.html')





@login_required(login_url="login")
def confirm(request):
    if request.method=="POST":
        uid=request.session.get('_auth_user_id')
        user=User.objects.get(id=uid)

        cart=request.session.get('cart')
        Firstname=request.POST.get("name_2")
        Lastname=request.POST.get("ls_1")
        Email=request.POST.get("Ea")
        state=request.POST.get("sc")
        Phone=request.POST.get("pho")
        post=request.POST.get("post")
        country=request.POST.get("country")
        Address=request.POST.get("sa")
        City=request.POST.get("ct")
       

        order=Order(
            user=user,
            Firstname=Firstname,
            Lastname=Lastname,
            Email=Email,
            State=state,
            Phone=Phone,
            Pincode=post,
            Country=country,
            Address=Address,
            City=City
            
        )

        order.save()

        for i in cart:
            a = float(cart[i]['price'])
            b = int(cart[i]['quantity'])
            total = a*b

            order1=OrderItem(
                order=order,
                product=cart[i]['name'],
                image=cart[i]['image'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                total=total

            )

            order1.save()
    return render(request, 'web/confirm.html')