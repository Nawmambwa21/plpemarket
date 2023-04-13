from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from .models import Products, Order, Orderitems


def store(request):
    products = Products.objects.all()
    context = { 'products': products }
    return render(request, 'store.html', context)

def cart(request):

        if request.user.is_authenticated :
            customer = request.user.customer
            order = Order.objects.get_or_create(customer=customer,complete=False)
            items = order.orderitem_set.all() 
        else:
           items = []
           order = {'get_cart_total':0, 'get_cart_items':0}
		
        context = {'items': items, 'order':order}
        return render(request, 'cart.html', context)

def checkout(request):
    
		if request.user.is_authenticated:
			customer=request.user.customer
			order = Order.objects.get_or_create(customer=customer, complete=False)
			items = Order.orderitem_set.all()
		else:
			order = {'get_cart_total':0, 'get_cart_items':0}


		context={}
		return render(request, 'cart.html', context)


def signup_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "signup successful." )
			return redirect("main:index")
	

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})
