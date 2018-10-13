from django.shortcuts import render, redirect
from models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
import datetime, decimal
from Employee.models import *
import traceback



# Create your views here.



@login_required
def dashboard(request):
	urlDashboard = True 
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	print request.session['userdata']
	if request.session['userdata']['type'] == "U":
		try:
			empObj = EmployeeMaster.objects.get(userId = userObj)
			if empObj.steps:
				return redirect('/employee/registration/'+ empObj.steps + '/')
		except:
			traceback.print_exc()
			pass
		return redirect('/employee/registration/myprofile/')

	vObj = EmployeeMaster.objects.all()

	return render(request, 'dashboard.html', locals())


