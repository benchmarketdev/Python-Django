from django.shortcuts import render, redirect
from Users.models import *
from Library.emailer import *
from Library.libre import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from Company.models import *
from datetime import datetime
from django.utils import timezone
import traceback
import string
import random



# Create your views here.



def register(request):
	if request.method =="POST":
		# print request.POST

		firstName = request.POST.get('fname')
		lastName = request.POST.get('lname')
		mobile = request.POST.get('mobile')
		email = request.POST.get('email')
		agree = request.POST.get('agree')

		password = request.POST.get('password')
		repassword = request.POST.get('repassword')

		estatus = 100
		if password != repassword:
			estatus = 101
		elif len(password)< 8 or password.isalnum():
			estatus = 102
		elif len(firstName)< 2 or len(lastName)< 2 or agree != 'on':
			estatus = 105
		
		if estatus == 100:
			try:			
				ip = get_client_ip(request)
				mac = get_client_mac(ip)

				userObj = Users(email = email, firstName = firstName, lastName = lastName, mobile = mobile, ipAddress = ip, macAddress = mac, isPassChanged = True, verificationCode = random_string(), otpSent = random.randint(100000,999999) )
				userObj.save()

				userObj.set_password(password)
				userObj.save()

				link = settings.SOFTWARE_URL +'/users/email-verification/?email=' + userObj.email +'&verification_code=' + userObj.verificationCode
				data = {'name': userObj.firstName, 'code': userObj.verificationCode, 'email': userObj.email, 'url': settings.SOFTWARE_URL, 'link': link}
				account_created_emailer(data)
				email_verification_emailer(data)

				return redirect('/users/email-verification/?email='+ userObj.email)

			except:
				# traceback.print_exc()
				estatus = 104
				pass
			
	return render(request, 'register.html', locals())



def email_verification(request):
	email = request.GET.get('email')
	verification_code = request.GET.get('verification_code')
	if email and verification_code:
		userObj = Users.objects.filter(email = email)
		
		if userObj:
			if userObj[0].verificationCode == verification_code:
				Users.objects.filter(pk = userObj[0].id).update(isEmailVerified = True, verifiedOn = datetime.now())

				data = {'name': userObj[0].firstName, 'email': userObj[0].email, 'url': settings.SOFTWARE_URL}
				email_verification_done_emailer(data)

				return redirect('/')
			else:
				estatus = 101
		else:
			estatus = 102

	return render(request, 'email-verification.html', locals())



def mobile_verification(request):	
	if request.method =="POST":
		mobile = request.POST.get('mobile')
		otpSent = request.POST.get('otp')

		userObj = Users.objects.get(pk = request.session['userdata']['userId'])
		if userObj:
			if userObj.otpSent == otpSent:
				userObj.isOTPVerified = True
				userObj.otpVerifiedOn = datetime.now()
				userObj.save()
				estatus = 103
			else:
				estatus = 101
		else:
			estatus = 102

	return render(request, 'mobile-verification.html', locals())





def signin(request):
	if request.method =="POST":
		if request.session.test_cookie_worked():
			request.session.delete_test_cookie()
			username = request.POST.get('username')
			password = request.POST.get('password')


			try:
				user = authenticate(username = username, password = password)
				# print user, password, username
			except:
				user = None
				pass

			if user is not None:
			    if user.isActive:
					login(request, user)

					# if not user.isOTPVerified:					

					access = []
					if user.is_admin:
						access.append('Admin')
					
					request.session['userdata'] = {"userId":user.id, "email": user.email, "name":user.firstName, "type": user.userType, "access": access}
					# print request.session['userdata'], user.userType
					
					ip = get_client_ip(request)
					mac = get_client_mac(ip)
					userLogin = UserLoginHistory( userId = user, ipAddress = ip, macAddress = mac )
					userLogin.save()
					# print user.isOTPVerified
					nxt = request.GET.get('next')
					# if not user.isOTPVerified:
					# 	return redirect('/users/mobile-verification/?mobile='+user.mobile)
					# elif not user.isEmailVerified:
					# 	estatus = 103
					if not user.isPassChanged:
						return redirect('/users/change-password/')
					elif nxt:
						return redirect(nxt)
					else:
						return redirect('/dashboard/')
			    else:
			        estatus = 102
			else:
			    estatus = 101
		
	request.session.set_test_cookie()
	return render(request, 'signin.html', locals())



@login_required
def change_password(request):
	if request.method =="POST":

		curpass = request.POST.get('curpass')
		newpass = request.POST.get('newpass')
		cnfpass = request.POST.get('cnfpass')

		estatus = 100
		if newpass != cnfpass:
			estatus = 101
		elif len(newpass)< 8 or newpass.isalnum():
			estatus = 102
		
		if estatus == 100:
			user = authenticate(username = request.session['userdata']['email'], password = curpass)
			if user is not None:
				user.set_password(newpass)
				user.isPassChanged = True
				user.save()
				return redirect('/')
			else:
				estatus = 103
			
	return render(request, 'change-password.html', locals())



@login_required
def signout(request):
	logout(request)
	return redirect('/')



def forgot_password(request):
	if request.method =="POST":
		email = request.POST.get('email')
		userObj = None

		try:
			userObj = Users.objects.get(email = email)
		except:
			pass

		if userObj:
			userObj.verificationCode = random_string()
			userObj.updatedOn = datetime.now()
			userObj.save()

			link = settings.SOFTWARE_URL +'/users/reset-password/?email=' + userObj.email +'&code=' + userObj.verificationCode
			data = {'name': userObj.firstName, 'email': userObj.email, 'link': link}
			forgot_password_emailer(data)

			estatus = 103
		else:
			estatus = 102

	return render(request, 'forgot-password.html', locals())






def reset_password(request):
	estatus = 100
	email = request.GET.get('email')
	code = request.GET.get('code')
	userObj = None
	try:
		userObj = Users.objects.get(email = email, verificationCode = code)
	except:
		pass

	if userObj:
		dtime = datetime.now() - userObj.updatedOn
		if dtime.seconds > 3600*24:
			estatus = 103

		if request.method =="POST":
			newpass = request.POST.get('newpass')
			cnfpass = request.POST.get('cnfpass')
			
			if newpass != cnfpass:
				estatus = 101
			elif len(newpass)< 8 or newpass.isalnum():
				estatus = 102
			
			if estatus == 100:
				userObj.set_password(newpass)
				userObj.save()
				return redirect('/')
			
	return render(request, 'reset-password.html', locals())




def tnc(request):	
	return render(request, 'tnc.html', locals())




def random_string(size=48, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))




