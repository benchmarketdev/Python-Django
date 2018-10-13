from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from Users.models import *
from datetime import datetime, date
from django.http import HttpResponse
import traceback
from django.db.models import Q
from random import randint
import csv
from pprint import pprint


# Create your views here.



@login_required
def myprofile(request):	
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	try:
		empObj = EmployeeMaster.objects.get(userId = userObj)					
	except:
		empObj = None
		pass

	if request.method =="POST":
		# print request.POST
		iD = request.POST.get('iD')
		surName = request.POST.get('surname')
		givenName = request.POST.get('givenname')

		fatherName = request.POST.get('fathername')
		motherName = request.POST.get('mothername')
		
		gender = request.POST.get('gender')	
		dateOfBirth = datetime.strptime(request.POST.get('dob'), "%d/%m/%Y").strftime("%Y-%m-%d")
		# dateOfBirth = request.POST.get('dob2')

		birthPlace = request.POST.get('birthpalce')		
		motherTongue = request.POST.get('mtongue')
		otherLanguages = request.POST.get('olanguages')	
		stateDomicile = request.POST.get('sdomicile')
		religion = request.POST.get('religion')
		maritalStatus = request.POST.get('mstatus')
		# numberChildren = request.POST.get('nchildren')
		# numberSiblings = request.POST.get('nsiblings')	
		bloodGroup = request.POST.get('bgroup')
		personalMobile = request.POST.get('pmobile')		
		personalEmail = request.POST.get('pemail')

		userPhoto = None
		if 'photo' in request.FILES:
			userPhoto = request.FILES['photo']
			if empObj:
				empObj.userPhoto = request.FILES['photo']

		signatureCopy = None
		if 'signature' in request.FILES:
			signatureCopy = request.FILES['signature']
			if empObj:
				empObj.signatureCopy = request.FILES['signature']
				

		try:
			if iD:
				empObj.save()
				empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(surName = surName, givenName = givenName, motherName = motherName, fatherName = fatherName, gender = gender, dateOfBirth = dateOfBirth, birthPlace = birthPlace, motherTongue = motherTongue, otherLanguages = otherLanguages, stateDomicile = stateDomicile, religion = religion, maritalStatus = maritalStatus, bloodGroup = bloodGroup, personalMobile = personalMobile, personalEmail = personalEmail, steps = 'mycontact', status = 'save' )
			else:
				empMasterObj = EmployeeMaster.objects.create(userId = userObj, surName = surName, givenName = givenName, motherName = motherName, fatherName = fatherName, gender = gender, dateOfBirth = dateOfBirth, birthPlace = birthPlace, motherTongue = motherTongue, otherLanguages = otherLanguages, stateDomicile = stateDomicile, religion = religion, maritalStatus = maritalStatus, bloodGroup = bloodGroup, personalMobile = personalMobile, personalEmail = personalEmail, userPhoto = userPhoto, signatureCopy = signatureCopy, steps = 'mycontact', status = 'save' )


			return redirect('/employee/registration/mycontact/')

		except:
			traceback.print_exc()
			pass
		

	return render(request, 'Employee/myprofile.html', locals())





@login_required
def mycontact(request):	
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	empObj = EmployeeMaster.objects.get(userId = userObj)
	try:
		prObj = EmployeePresentAddress.objects.get(employeeId = empObj)
		pmObj = EmployeePermanentAddress.objects.get(employeeId = empObj)
		emObj = EmployeeEmergencyContact.objects.get(employeeId = empObj)
	except:
		pass
	
	
	if request.method =="POST":
		# print request.POST
		iD = request.POST.get('iD')
		praddress1 = request.POST.get('praddress1')	 
		praddress2 = request.POST.get('praddress2')
		prcity = request.POST.get('prcity')	
		prstate = request.POST.get('prstate')
		prcountry = request.POST.get('prcountry')
		prpin = request.POST.get('prpin')

		pmaddress1 = request.POST.get('pmaddress1')	
		pmaddress2 = request.POST.get('pmaddress2')
		pmcity = request.POST.get('pmcity')	
		pmstate = request.POST.get('pmstate')
		pmcountry = request.POST.get('pmcountry')
		pmpin = request.POST.get('pmpin')

		name = request.POST.get('name')	
		relation = request.POST.get('relation')
		mobile = request.POST.get('mobile')
		phone = request.POST.get('phone')
		address1 = request.POST.get('address1')	
		address2 = request.POST.get('address2')
		city = request.POST.get('city')	
		state = request.POST.get('state')
		country = request.POST.get('country')
		pin = request.POST.get('pin')

		try:
			if iD:
				# empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'myid', status = 'save' )

				prAddObj = EmployeePresentAddress.objects.filter(employeeId = empObj).update( address1 = praddress1, address2 = praddress2, city = prcity, state = prstate, country = prcountry, pin = prpin )

				pmAddObj = EmployeePermanentAddress.objects.filter(employeeId = empObj).update( address1 = pmaddress1, address2 = pmaddress2, city = pmcity, state = pmstate, country = pmcountry, pin = pmpin )

				emAddObj = EmployeeEmergencyContact.objects.filter(employeeId = empObj).update( name = name, relation = relation, mobile = mobile, phone = phone, address1 = address1, address2 = address2, city = city, state = state, country = country, pin = pin )

			else:
				empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'myid', status = 'save' )

				prAddObj = EmployeePresentAddress.objects.create(employeeId = empObj, address1 = praddress1, address2 = praddress2, city = prcity, state = prstate, country = prcountry, pin = prpin )

				pmAddObj = EmployeePermanentAddress.objects.create(employeeId = empObj, address1 = pmaddress1, address2 = pmaddress2, city = pmcity, state = pmstate, country = pmcountry, pin = pmpin )

				emAddObj = EmployeeEmergencyContact.objects.create(employeeId = empObj, name = name, mobile = mobile, phone = phone, relation = relation, address1 = address1, address2 = address2, city = city, state = state, country = country, pin = pin )

			return redirect('/employee/registration/myid/')

		except:
			traceback.print_exc()
			pass
				

	return render(request, 'Employee/mycontact.html', locals())




@login_required
def myid(request):	
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	empObj = EmployeeMaster.objects.get(userId = userObj)
	try:
		idObj = EmployeeIDProof.objects.get(employeeId = empObj)
	except:
		idObj = None
		pass

	if request.method =="POST":
		print request.POST, request.FILES
		iD = request.POST.get('iD')
		aadharNumber = request.POST.get('aadhar')		
		panNumber = request.POST.get('pan')
		dlNumber = request.POST.get('dl')
		voterNumber = request.POST.get('voter')
		passportNumber = request.POST.get('passport')

		aadharCopy = None
		if 'addhas' in request.FILES:
			aadharCopy = request.FILES['addhas']
			if idObj:
				idObj.aadharCopy = request.FILES['addhas']

		panCopy = None
		if 'pans' in request.FILES:
			panCopy = request.FILES['pans']
			if idObj:
				idObj.panCopy = request.FILES['pans']

		dlCopy = None
		if 'dls' in request.FILES:
			dlCopy = request.FILES['dls']
			if idObj:
				idObj.dlCopy = request.FILES['dls']

		voterCopy = None
		if 'voters' in request.FILES:
			voterCopy = request.FILES['voters']
			if idObj:
				idObj.voterCopy = request.FILES['voters']

		passportCopy = None
		if 'passports' in request.FILES:
			passportCopy = request.FILES['passports']
			if idObj:
				idObj.passportCopy = request.FILES['passports']

		try:
			if iD:
				idObj.save()
				idsObj = EmployeeIDProof.objects.filter(employeeId = empObj).update( aadharNumber = aadharNumber, panNumber = panNumber, dlNumber = dlNumber, voterNumber = voterNumber, passportNumber = passportNumber )

			else:
				empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'myfamily', status = 'save' )

				idsObj = EmployeeIDProof.objects.create(employeeId = empObj, aadharNumber = aadharNumber, aadharCopy = aadharCopy, panNumber = panNumber, panCopy = panCopy, dlNumber = dlNumber, dlCopy = dlCopy, voterNumber = voterNumber, voterCopy = voterCopy, passportNumber = passportNumber, passportCopy = passportCopy )

			return redirect('/employee/registration/myfamily/')

		except:
			traceback.print_exc()
			pass		

	return render(request, 'Employee/myid.html', locals())




@login_required
def myfamily(request):
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	empObj = EmployeeMaster.objects.get(userId = userObj)
	try:
		fmObj = EmployeeFamilyDetails.objects.filter(employeeId = empObj)
	except:
		pass

	if request.method =="POST":
		print request.POST

		try:
			for x in range(1,6):
				name = request.POST.get('name'+`x`)		
				if name:
					iD = request.POST.get('iD'+`x`)
					relation = request.POST.get('relation'+`x`)
					mobile = request.POST.get('mobile'+`x`)
					phone = request.POST.get('phone'+`x`)
					fullAddress = request.POST.get('faddress'+`x`)

					dateOfBirth = datetime.strptime(request.POST.get('dob'+`x`), "%d/%m/%Y").strftime("%Y-%m-%d") if request.POST.get('dob'+`x`) else None
					occupation = request.POST.get('occupation'+`x`)
					organisation = request.POST.get('organization'+`x`)

					isDependent = True if request.POST.get('dependent'+`x`) == 'YES' else False
					isPFNominee = True if request.POST.get('pf'+`x`) == 'Y' else False
					isBFNominee = True if request.POST.get('bf'+`x`) == 'Y' else False
					isGFNominee = True if request.POST.get('gf'+`x`) == 'Y' else False
					isESICNominee = True if request.POST.get('esic'+`x`) == 'Y' else False

					pfPercentage = request.POST.get('ppf'+`x`) if request.POST.get('ppf'+`x`) else 0
					bfPercentage = request.POST.get('pbf'+`x`) if request.POST.get('pbf'+`x`) else 0
					gfPercentage = request.POST.get('pgf'+`x`) if request.POST.get('pgf'+`x`) else 0
					esicPercentage = request.POST.get('pesic'+`x`) if request.POST.get('pesic'+`x`) else 0

					if iD:
						fObj = EmployeeFamilyDetails.objects.filter(id = iD).update( name = name, relation = relation, fullAddress = fullAddress, mobile = mobile, phone = phone, dateOfBirth = dateOfBirth, occupation = occupation, organisation = organisation, isDependent = isDependent, isPFNominee = isPFNominee, pfPercentage = pfPercentage, isBFNominee = isBFNominee, bfPercentage = bfPercentage, isGFNominee = isGFNominee, gfPercentage = gfPercentage, isESICNominee = isESICNominee, esicPercentage = esicPercentage )

					else:
						empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'myacademic', status = 'save' )

						fObj = EmployeeFamilyDetails.objects.create(employeeId = empObj, name = name, relation = relation, fullAddress = fullAddress, mobile = mobile, phone = phone, dateOfBirth = dateOfBirth, occupation = occupation, organisation = organisation, isDependent = isDependent, isPFNominee = isPFNominee, pfPercentage = pfPercentage, isBFNominee = isBFNominee, bfPercentage = bfPercentage, isGFNominee = isGFNominee, gfPercentage = gfPercentage, isESICNominee = isESICNominee, esicPercentage = esicPercentage )

			return redirect('/employee/registration/myacademic/')

		except:
			traceback.print_exc()
			pass	
		

	return render(request, 'Employee/myfamily.html', locals())




@login_required
def myacademic(request):	
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	empObj = EmployeeMaster.objects.get(userId = userObj)
	acObj = EmployeeAcademicDetails.objects.filter(employeeId = empObj)
	
	if request.method =="POST":
		print request.POST

		try:
			for x in range(1,5):
				qualification = request.POST.get('qualification'+`x`)		
				if qualification:
					iD = request.POST.get('iD'+`x`)
					subjects = request.POST.get('subjects'+`x`)
					passingYear = request.POST.get('passing'+`x`)
					perOrGrade = request.POST.get('percent'+`x`)
					institute = request.POST.get('institute'+`x`)
					
					certificateCopy = None
					if 'certificate'+`x` in request.FILES:
						certificateCopy = request.FILES['certificate'+`x`]

					if iD:
						qObj = EmployeeAcademicDetails.objects.get(id = iD)
						qObj.qualification = qualification
						qObj.subjects = subjects
						qObj.passingYear = passingYear
						qObj.perOrGrade = perOrGrade
						qObj.institute = institute
						if certificateCopy:
							qObj.certificateCopy = request.FILES['certificate'+`x`]
						qObj.save()

					else:
						empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'myexperiance', status = 'save' )

						qObj = EmployeeAcademicDetails.objects.create(employeeId = empObj, qualification = qualification, subjects = subjects, passingYear = passingYear, perOrGrade = perOrGrade, institute = institute, certificateCopy = certificateCopy )

			return redirect('/employee/registration/myexperiance/')

		except:
			traceback.print_exc()
			pass	
		

	return render(request, 'Employee/myacademic.html', locals())




@login_required
def myexperiance(request):	
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	empObj = EmployeeMaster.objects.get(userId = userObj)
	expObj = EmployeeExperienceDetails.objects.filter(employeeId = empObj)
	
	if request.method =="POST":
		print request.POST

		try:
			for x in range(1,4):
				company = request.POST.get('company'+`x`)		
				if company:
					iD = request.POST.get('iD'+`x`)
					address = request.POST.get('address'+`x`)
					designation = request.POST.get('designation'+`x`)
					reportingTo = request.POST.get('reporting'+`x`)
					contactNumber = request.POST.get('contact'+`x`)
					lastDrawnSalary = request.POST.get('salary'+`x`)
					dateOfJoining = datetime.strptime(request.POST.get('doj'+`x`), "%d/%m/%Y").strftime("%Y-%m-%d") if request.POST.get('doj'+`x`) else None
					dateOfRelieving = datetime.strptime(request.POST.get('dor'+`x`), "%d/%m/%Y").strftime("%Y-%m-%d") if request.POST.get('dor'+`x`) else None
					totalTime = request.POST.get('time'+`x`)
					reasonForSeparation = request.POST.get('reason'+`x`)

					paySlipCopy = None
					if 'payslip'+`x` in request.FILES:
						paySlipCopy = request.FILES['payslip'+`x`]

					relievingCopy = None
					if 'relieving'+`x` in request.FILES:
						relievingCopy = request.FILES['relieving'+`x`]

					if iD:
						eObj = EmployeeExperienceDetails.objects.get(id = iD)
						eObj.company = company
						eObj.address = address
						eObj.designation = designation
						eObj.reportingTo = reportingTo
						eObj.contactNumber = contactNumber
						eObj.lastDrawnSalary = lastDrawnSalary
						eObj.dateOfJoining = dateOfJoining
						eObj.dateOfRelieving = dateOfRelieving
						eObj.totalTime = totalTime
						eObj.reasonForSeparation = reasonForSeparation
						if paySlipCopy:
							eObj.paySlipCopy = paySlipCopy
						if relievingCopy:
							eObj.relievingCopy = relievingCopy
						eObj.save()


					else:
						empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'account', status = 'save' )

						eObj = EmployeeExperienceDetails.objects.create(employeeId = empObj, company = company, address = address, designation = designation, reportingTo = reportingTo, contactNumber = contactNumber, lastDrawnSalary = lastDrawnSalary, dateOfJoining = dateOfJoining, dateOfRelieving = dateOfRelieving, totalTime = totalTime, reasonForSeparation = reasonForSeparation, paySlipCopy = paySlipCopy, relievingCopy = relievingCopy )

			return redirect('/employee/registration/account/')

		except:
			traceback.print_exc()
			pass
		

	return render(request, 'Employee/myexperiance.html', locals())






@login_required
def account(request):	
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	empObj = EmployeeMaster.objects.get(userId = userObj)
	try:
		acObj = EmployeeBankDetails.objects.get(employeeId = empObj)
	except:
		pass

	if request.method =="POST":
		print request.POST
		iD = request.POST.get('iD')

		try:
			bankAccount = request.POST.get('account')	
			bankName = request.POST.get('bank')	
			ifscCode = 	request.POST.get('ifsc')

			if iD:
				rObj = EmployeeBankDetails.objects.filter(employeeId = empObj).update( bankAccount = bankAccount, bankName = bankName, ifscCode = ifscCode )

			else:
				empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'peopleknowsme', status = 'submit' )

				rObj = EmployeeBankDetails.objects.create(employeeId = empObj, bankAccount = bankAccount, bankName = bankName, ifscCode = ifscCode )

			return redirect('/employee/registration/peopleknowsme/')

		except:
			traceback.print_exc()
			pass	
		

	return render(request, 'Employee/account.html', locals())






@login_required
def peopleknowsme(request):	
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	empObj = EmployeeMaster.objects.get(userId = userObj)
	peoObj = EmployeeReferenceDetails.objects.filter(employeeId = empObj)
	
	if request.method =="POST":
		print request.POST

		try:
			for x in range(1,3):
				fullName = request.POST.get('name'+`x`)		
				if fullName:
					iD = request.POST.get('iD'+`x`)
					fatherName = request.POST.get('father'+`x`)
					fullAddress = request.POST.get('address'+`x`)
					phoneNumber = request.POST.get('mobile'+`x`)
					email = request.POST.get('email'+`x`)
					knownFromDate = datetime.strptime(request.POST.get('kfd'+`x`), "%d/%m/%Y").strftime("%Y-%m-%d") if request.POST.get('kfd'+`x`) else None
					
					idProofCopy = None
					if 'id'+`x` in request.FILES:
						idProofCopy = request.FILES['id'+`x`]

					if iD:
						pObj = EmployeeReferenceDetails.objects.get(id = iD)
						pObj.fullName = fullName
						pObj.fullAddress = fullAddress
						pObj.phoneNumber = phoneNumber
						pObj.email = email
						pObj.knownFromDate = knownFromDate
						if idProofCopy:
							pObj.idProofCopy = idProofCopy
						pObj.save()

					else:
						empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'staffknowsme', status = 'save' )

						pObj = EmployeeReferenceDetails.objects.create(employeeId = empObj, fullName = fullName, fullAddress = fullAddress, phoneNumber = phoneNumber, email = email, knownFromDate = knownFromDate, idProofCopy = idProofCopy )

			return redirect('/employee/registration/staffknowsme/')

		except:
			traceback.print_exc()
			pass	
		

	return render(request, 'Employee/peopleknowsme.html', locals())





@login_required
def staffknowsme(request):	
	userObj = Users.objects.get(pk = request.session['userdata']['userId'])
	empObj = EmployeeMaster.objects.get(userId = userObj)
	try:
		refObj = EmployeeReferralDetails.objects.get(employeeId = empObj)
	except:
		pass

	if request.method =="POST":
		print request.POST
		iD = request.POST.get('iD')

		try:
			referralName = request.POST.get('staffname')	
			referralEmpCode = request.POST.get('staffid')					

			if iD:
				rObj = EmployeeReferralDetails.objects.filter(id = iD).update( referralName = referralName, referralEmpCode = referralEmpCode )

			else:
				empMasterObj = EmployeeMaster.objects.filter(userId = userObj).update(steps = 'thankyou', status = 'submit' )

				rObj = EmployeeReferralDetails.objects.create(employeeId = empObj, referralName = referralName, referralEmpCode = referralEmpCode )

			return redirect('/employee/registration/thankyou/')

		except:
			traceback.print_exc()
			pass	
		

	return render(request, 'Employee/staffknowsme.html', locals())




@login_required
def thankyou(request):	
	
	return render(request, 'Employee/thankyou.html', locals())





