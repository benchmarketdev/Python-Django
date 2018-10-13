from django.shortcuts import render, redirect
from models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
import datetime, decimal
from Employee.models import *
from Library.emailer import *
from Users.models import *
from django.db.models import Q



# Create your views here.



@login_required
def newjoining(request):
	urlNewJoining = True 

	if request.method =="POST":
		# print request.POST

		firstName = request.POST.get('fname')
		lastName = request.POST.get('lname')
		email = request.POST.get('email')
		mobile = request.POST.get('mobile')

		# empCode = request.POST.get('empcode')
		# location = request.POST.get('location')
		# department = request.POST.get('department')
		# designation = request.POST.get('designation')
		# band = request.POST.get('band')		

		try:
			cUser = Users.objects.filter(Q(email=email) | Q(mobile=mobile))
			if not cUser:
				userObj = Users(email = email, firstName = firstName, lastName = lastName, mobile = mobile,  isPassChanged = False )
				userObj.save()

				empObj = EmployeeMaster.objects.create( userId = userObj, surName = lastName, givenName = firstName, personalMobile = mobile, personalEmail = email, motherName = '', fatherName = '', birthPlace = '', motherTongue = '', otherLanguages = '', stateDomicile = '', religion = '', bloodGroup = '' )				
				
				userObj.set_password(mobile)
				userObj.save()


				link = settings.SOFTWARE_URL
				data = {'name': userObj.firstName, 'email': userObj.email, 'url': settings.SOFTWARE_URL, 'link': link}
				account_created_emailer(data) 

				estatus = 100
			else:
				estatus = 102

		except:
			traceback.print_exc()
			estatus = 104
			pass
	

	return render(request, 'Joining/new.html', locals())





