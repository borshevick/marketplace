from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from marketplace.models import *
from marketplace.forms import *




@login_required
def cart(request):
    items = request.user.cart.items.all()
    return render(request, "cart.html", {'items':items})

@login_required
def item(request, item_id):
    item = Item.objects.get(id = item_id)
    return render(request, "item.html", {'item':item})

@login_required
def itemsList(request):
    items = Item.objects.all()
    return render(request, "main.html", {'items':items})

def my_login(request):
    if request.method == "GET":
        response = render(request, "login.html")
        return response
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        object = authenticate(request, username = username, password = password)
        if object != None:
            login(request, object)
            return redirect("main")
        else:
            return render(request, "login.html")
        
def my_logout(request):
    logout(request)
    return redirect("main")

@login_required
def profile(request):
    return render(request, "profile.html")

def reg(request):
    if request.method == "GET":
        form = RegForm()
        return render(request, "reg.html", {"form":form})
    else:
        form = RegForm(request.POST)
        if form.is_valid() == True:
            user = form.save()
            Cart.objects.create(user = user)
            login(request, user)
            return redirect("main")
        else:
            return render(request, "reg.html", {"form":form})



@login_required
def add_to_cart(request):
    id = request.POST['item_id']
    id = int(id)
    item = Item.objects.get(id = id)
    request.user.cart.items.add(item)
    return redirect("main")