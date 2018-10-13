from django.shortcuts import render, redirect
from .models import Users
from django.contrib import messages
import re
import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):	
	return render(request, "main_app/index.html")

def process(request):
	if request.method == 'POST':
		new_user = Users.objects.AddUser(
			request.POST['first_name'],
			request.POST['last_name'], 
			request.POST['email'],
			request.POST['password'],
			request.POST['confirm']
			)
		if type(new_user) is list:
			for error in new_user:
				messages.add_message(request, messages.ERROR, error)
			return redirect('/')
		else:
			request.session['user_id'] = new_user.id
			request.session['user_name'] = new_user.first_name
			request.session['success'] = 'registered'
			return redirect("/success")
	else:
		return redirect("/")		

def login(request):	
	if request.method == 'POST':
		login = Users.objects.login(
			request.POST['email'],
			request.POST['password']
			)
		if type(login) is unicode:
			messages.add_message(request, messages.ERROR, login)
			return redirect('/')
		else:
			request.session['user_id'] = login.id
			request.session['user_name'] = login.first_name
			request.session['success'] = 'logged in'
			return redirect("/success")
		return redirect("/")
	else:
		return redirect("/")	

def logout(request):
	request.session.clear()	
	return redirect('/')

def success(request):
	if 'user_id' not in request.session:
		return redirect('/')
	else:	
		return render(request, "main_app/success.html")		
