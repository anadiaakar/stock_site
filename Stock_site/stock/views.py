from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse , JsonResponse
from .models import Stocks
from stock.forms import StockForm , UserForm
import sys,os
from django.core import serializers

# Create your views here.

class CreateListings(View):
	def get(self,request):
		if request.user.is_authenticated:
			form = StockForm()
			return render(request,'form.html',{'form' : form})
	
	def post(self,request):
		values = StockForm(request.POST)
		if values.is_valid:
			values.save()
			req_stocks = Stocks.objects.all.order_by('-id')[:5]
			return render(request,'home.html',{'data' : req_stocks})
		return JsonResponse({'data':"Unable to validate form"})

class Stock(View):
	def get(self,request):
		if request.user.is_authenticated:
			id = request.GET["id"]
			stock = Stocks.objects.get(id = id)
			return render(request,'view.html',{'data' : stock})
		return render(request,'home.html',{'data':False,'message1': 'Please login to view this'})

class Listings(View):
	def get(self,request):
		if request.user.is_authenticated:
			req_stocks = Stocks.objects.all().order_by('-id')[:5]

			return render(request,'home.html',{'data':req_stocks,'login': '1'})
		else:

			return render(request,'home.html',{'data':False,'login':'0'})

	def post(self,request):
		try:
			last_val = int(request.POST['last_val'])
			
			req_stocks = Stocks.objects.all().order_by('-id')[last_val:last_val+5]
			req_stocks = serializers.serialize('json', req_stocks)
			return JsonResponse({'data':req_stocks})
		except Exception as e:
			print(e)
			exc_type, exc_obj, exc_tb = sys.exc_info()
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			print(exc_type, fname, exc_tb.tb_lineno)

	

class Login(View):
	def get(self,request):
		return render(request,'login.html',{})

	def post(self,request):
		user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
		if user:
			login(request, user)
			return HttpResponseRedirect("/home")
		else:
			return render(request,'login.html',{"error":"User Credentials not valid"})


class SignUp(View):
	def get(self,request):
		form = UserForm()
		return render(request,'signup.html',{'form':form})

	def post(self,request):
		form = UserForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			new_user.set_password(new_user.password)
			new_user.save()

		return render(request,'login.html', {})

class Logout(View):
    def get(self, request):
        logout(request)        
        return HttpResponseRedirect("/")

