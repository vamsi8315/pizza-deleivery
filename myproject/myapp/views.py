from django.shortcuts import render,redirect
from django.contrib import messages
#from django.contrib.auth import authenticate,login,logout
#from django.contrib.auth.models import User
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from myapp.forms import Myform
from django.contrib.auth.decorators import login_required
from myapp.models import PizzaModel,OrderModel

# Create your views here.
def register(request):
	if request.method=="POST":
		data=Myform(request.POST)
		if data.is_valid():
			data.save()
			return HttpResponse("<h1>data is saved</h1>")
		else:
			return HttpResponse("<h1> go back and check your details </h1>")
	form=Myform()
	return render(request,'myapp/register.html',{'form':form})
@login_required
def home(request):
	
	username = request.user.username
	context = {'username' : username,'pizzas' : PizzaModel.objects.all()}
	return render(request,'myapp/home.html',context)
def placeorder(request):
	if not request.user.is_authenticated:
		return redirect('myapp/login.html')

	username = request.user.username
	address = request.POST['address']
	ordereditems = ""
	for pizza in PizzaModel.objects.all():
		pizzaid = pizza.id
		name = pizza.name
		price = pizza.price

		quantity = request.POST.get(str(pizzaid)," ")




		if str(quantity)!="0" and str(quantity)!=" ":
			ordereditems = ordereditems + name+" " + "price : " + str(int(quantity)*int(price)) +" "+ "quantity : "+ quantity+"    "

	print(ordereditems)
	OrderModel(username = username,address = address,ordereditems = ordereditems).save()
	#OrderModel(username = username,address = address,ordereditems = ordereditems).save()
	messages.add_message(request,messages.ERROR,"order succesfully placed")
#	data=PizzaModel.objects.all()
	return redirect('/home')
def adminloginpage(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		if(username=="admin" and password=="vamsi"):
			return redirect("/adminhome")
		else:
			return HttpResponse("go back and check your admin details")
	return render(request,'myapp/adminloginpage.html')
def adminhome(request):
	context = {'pizzas' : PizzaModel.objects.all()}
	#return render(request,"pizzaapp/adminhomepage.html",context)
	
	return render(request,"myapp/adminhome.html",context)
def addpizza(request):
	# write a code to add the pizza into the database
	name = request.POST['pizza']
	price = request.POST['price']
	PizzaModel(name = name,price = price).save()
	return redirect('/adminhome')
def deletepizza(request,pizzapk):
	PizzaModel.objects.filter(id = pizzapk).delete()
	return redirect(request,'myapp/adminhome.html')
def userorders(request):
	orders = OrderModel.objects.filter(username = request.user.username)
	context = {'orders' : orders}
	return render(request,'myapp/userorders.html',context)
def adminorders(request):
	orders = OrderModel.objects.all()
	context = {'orders' : orders}
	return render(request,'myapp/adminorders.html',context)