from django.db import models
from Company.models import *
from django.conf import settings
from Users.models import Users
from Location.models import *
from General.models import *



# Create your models here.



class EmployeeMaster(models.Model):	
	userId = models.ForeignKey(settings.AUTH_USER_MODEL, null = True, blank = True)
	empCode = models.CharField(max_length = 10, null = True, blank = True, db_index = True)
	locationId = models.ForeignKey(Location, null = True, blank = True)
	departmentId = models.ForeignKey(Department, null = True, blank = True)
	designationId = models.ForeignKey(Designation, null = True, blank = True)
	bandId = models.ForeignKey(Band, null = True, blank = True)

	location = models.CharField(max_length = 10, null = True, blank = True)
	department = models.CharField(max_length = 10, null = True, blank = True)
	designation = models.CharField(max_length = 100, null = True, blank = True)
	band = models.CharField(max_length = 10, null = True, blank = True)

	roleId = models.ForeignKey(Role, null = True, blank = True)
	reportToEmpId = models.ForeignKey('self', related_name='report_to', null = True, blank = True)
	reportToEmpCode = models.CharField(max_length = 10, null = True, blank = True, db_index = True)
	reportToEmpName = models.CharField(max_length = 100, null = True, blank = True)
	dateOfJoining = models.DateField(null = True, blank = True)

	surName = models.CharField(max_length = 200, db_index = True)
	givenName = models.CharField(max_length = 200, db_index = True, null = True, blank = True)

	fatherName = models.CharField(max_length = 200, db_index = True, null = True, blank = True)
	motherName = models.CharField(max_length = 200, db_index = True, null = True, blank = True)

	gender = models.CharField(max_length = 1, null = True, blank = True)    # M/F
	dateOfBirth = models.DateField(null = True, blank = True)

	birthPlace = models.CharField(max_length = 100, null = True, blank = True)
	motherTongue = models.CharField(max_length = 100, null = True, blank = True)
	otherLanguages = models.CharField(max_length = 200, null = True, blank = True)

	stateDomicile = models.CharField(max_length = 100, null = True, blank = True)
	religion = models.CharField(max_length = 100, null = True, blank = True)
	maritalStatus = models.CharField(max_length = 100, null = True, blank = True)

	numberChildren = models.CharField(max_length = 2, null = True, blank = True)
	numberSiblings = models.CharField(max_length = 2, null = True, blank = True)

	bloodGroup = models.CharField(max_length = 20, null = True, blank = True)

	personalMobile = models.CharField(max_length = 100, db_index = True, null = True, blank = True)
	personalEmail = models.EmailField(max_length = 255, db_index = True, null = True, blank = True)

	userPhoto = models.ImageField(upload_to="static/private/employee/photos/%Y/%m/", null=True, blank=True)
	signatureCopy = models.FileField(upload_to="static/private/employee/files/signature/%Y/%m/", null=True, blank=True)
	thumbImpressionCopy = models.FileField(upload_to="static/private/employee/files/thumbimpression/%Y/%m/", null=True, blank=True)

	steps = models.CharField(max_length = 20, null = True, blank = True)
	status = models.CharField(max_length = 10, null = True, blank = True) # save/submit
	
	isActive = models.BooleanField(default = True)
	isDeleted = models.BooleanField(default = False)

	addedOn = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	addedBy = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='EmployeeMasterAddedByUser')

	updatedOn = models.DateTimeField(auto_now = True, null = True, blank = True)
	updatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='EmployeeMasterUpdatedByUser')



class EmployeeIDProof(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)

	aadharNumber = models.CharField(max_length = 50, null = True, blank = True)
	aadharCopy = models.FileField(upload_to="static/private/employee/files/aadhar/%Y/%m/", null=True, blank=True)

	panNumber = models.CharField(max_length = 50, null = True, blank = True)
	panCopy = models.FileField(upload_to="static/private/employee/files/pan/%Y/%m/", null=True, blank=True)

	dlNumber = models.CharField(max_length = 50, null = True, blank = True)
	dlCopy = models.FileField(upload_to="static/private/employee/files/dl/%Y/%m/", null=True, blank=True)

	voterNumber = models.CharField(max_length = 50, null = True, blank = True)
	voterCopy = models.FileField(upload_to="static/private/employee/files/dl/%Y/%m/", null=True, blank=True)

	passportNumber = models.CharField(max_length = 50, null = True, blank = True)
	passportCopy = models.FileField(upload_to="static/private/employee/files/passport/%Y/%m/", null=True, blank=True)



class EmployeeSocialInfo(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	facebook = models.CharField(max_length = 255, null = True, blank = True)
	linkedin = models.CharField(max_length = 255, null = True, blank = True)



class EmployeeBankDetails(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	bankAccount = models.CharField(max_length = 25, null = True, blank = True)
	bankName = models.CharField(max_length = 100, null = True, blank = True)
	ifscCode = models.CharField(max_length = 25, null = True, blank = True)



class EmployeePresentAddress(models.Model):	
	employeeId = models.ForeignKey(EmployeeMaster)
	address1 = models.CharField(max_length = 255, null = True, blank = True)
	address2 = models.CharField(max_length = 255, null = True, blank = True)
	city = models.CharField(max_length = 50, null = True, blank = True)
	state = models.CharField(max_length = 50, null = True, blank = True)
	country = models.CharField(max_length = 50, null = True, blank = True)
	pin = models.CharField(max_length = 20, null = True, blank = True)



class EmployeePermanentAddress(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	address1 = models.CharField(max_length = 255, null = True, blank = True)
	address2 = models.CharField(max_length = 255, null = True, blank = True)
	city = models.CharField(max_length = 50, null = True, blank = True)
	state = models.CharField(max_length = 50, null = True, blank = True)
	country = models.CharField(max_length = 50, null = True, blank = True)
	pin = models.CharField(max_length = 20, null = True, blank = True)



class EmployeeEmergencyContact(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	name = models.CharField(max_length = 255, null = True, blank = True)
	relation = models.CharField(max_length = 25, null = True, blank = True)
	mobile = models.CharField(max_length = 100, null = True, blank = True)
	phone = models.CharField(max_length = 100, null = True, blank = True)  
	address1 = models.CharField(max_length = 255, null = True, blank = True)
	address2 = models.CharField(max_length = 255, null = True, blank = True)
	city = models.CharField(max_length = 50, null = True, blank = True)
	state = models.CharField(max_length = 50, null = True, blank = True)
	country = models.CharField(max_length = 50, null = True, blank = True)
	pin = models.CharField(max_length = 20, null = True, blank = True)



class EmployeeFamilyDetails(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	name = models.CharField(max_length = 255, null = True, blank = True)
	relation = models.CharField(max_length = 25, null = True, blank = True)
	fullAddress = models.TextField(max_length = 255, null = True, blank = True)
	mobile = models.CharField(max_length = 100, null = True, blank = True)
	phone = models.CharField(max_length = 100, null = True, blank = True)  
	dateOfBirth = models.DateField(max_length = 100, null = True, blank = True)	
	occupation = models.CharField(max_length = 100, null = True, blank = True)
	organisation = models.CharField(max_length = 255, null = True, blank = True)
	isDependent = models.BooleanField(default = False)
	isPFNominee = models.BooleanField(default = False)
	pfPercentage = models.SmallIntegerField(default = 0)
	isBFNominee = models.BooleanField(default = False)
	bfPercentage = models.SmallIntegerField(default = 0)
	isGFNominee = models.BooleanField(default = False)
	gfPercentage = models.SmallIntegerField(default = 0)
	isESICNominee = models.BooleanField(default = False)
	esicPercentage = models.SmallIntegerField(default = 0)
	
	bankAccount = models.CharField(max_length = 25, null = True, blank = True)
	bankName = models.CharField(max_length = 100, null = True, blank = True)
	branchName = models.CharField(max_length = 100, null = True, blank = True)
	ifscCode = models.CharField(max_length = 25, null = True, blank = True)
	idCopy = models.FileField(upload_to="static/private/employee/nominee/files/id/%Y/%m/", null=True, blank=True)
	photo = models.ImageField(upload_to="static/private/employee/nominee/files/photo/%Y/%m/", null=True, blank=True)



class EmployeeNomineeDetails(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	familyId = models.ForeignKey(EmployeeFamilyDetails)
	isDependent = models.BooleanField(default = False)
	isPFNominee = models.BooleanField(default = False)
	pfPercentage = models.SmallIntegerField(default = 0)
	isBFNominee = models.BooleanField(default = False)
	bfPercentage = models.SmallIntegerField(default = 0)
	isGFNominee = models.BooleanField(default = False)
	gfPercentage = models.SmallIntegerField(default = 0)
	isESICNominee = models.BooleanField(default = False)
	esicPercentage = models.SmallIntegerField(default = 0)
	bankAccount = models.CharField(max_length = 25, null = True, blank = True)
	bankName = models.CharField(max_length = 100, null = True, blank = True)
	ifscCode = models.CharField(max_length = 25, null = True, blank = True)
	aadharNumber = models.CharField(max_length = 50, null = True, blank = True)
	aadharCopy = models.FileField(upload_to="static/private/employee/nominee/files/aadhar/%Y/%m/", null=True, blank=True)
	residenceCopy = models.FileField(upload_to="static/private/employee/nominee/files/residence/%Y/%m/", null=True, blank=True)
	photo = models.ImageField(upload_to="static/private/employee/nominee/files/photo/%Y/%m/", null=True, blank=True)



class EmployeeAcademicDetails(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	qualification = models.CharField(max_length = 25, null = True, blank = True)
	subjects = models.CharField(max_length = 255, null = True, blank = True)
	passingYear = models.SmallIntegerField(default = 0)
	institute = models.CharField(max_length = 255, null = True, blank = True)
	perOrGrade = models.CharField(max_length = 25, null = True, blank = True)
	certificateCopy = models.FileField(upload_to="static/private/employee/files/certificate/%Y/%m/", null=True, blank=True)



class EmployeeExperienceDetails(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	company = models.CharField(max_length = 255, null = True, blank = True)
	address = models.CharField(max_length = 255, null = True, blank = True)
	designation = models.CharField(max_length = 50, null = True, blank = True)
	reportingTo = models.CharField(max_length = 255, null = True, blank = True)
	contactNumber = models.CharField(max_length = 50, null = True, blank = True)
	lastDrawnSalary = models.CharField(max_length = 10, null = True, blank = True)
	dateOfJoining = models.DateField(null = True, blank = True)
	dateOfRelieving = models.DateField(null = True, blank = True)
	totalTime = models.CharField(max_length = 50, null = True, blank = True)
	reasonForSeparation = models.CharField(max_length = 255, null = True, blank = True)
	paySlipCopy = models.FileField(upload_to="static/private/employee/files/payslip/%Y/%m/", null=True, blank=True)
	relievingCopy = models.FileField(upload_to="static/private/employee/files/relieving/%Y/%m/", null=True, blank=True)
	


class EmployeeReferenceDetails(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	fullName = models.CharField(max_length = 255, null = True, blank = True)
	fatherName = models.CharField(max_length = 255, null = True, blank = True)
	fullAddress = models.CharField(max_length = 255, null = True, blank = True)
	company = models.CharField(max_length = 255, null = True, blank = True)
	designation =  models.CharField(max_length = 50, null = True, blank = True)
	officeAddress =  models.CharField(max_length = 255, null = True, blank = True)
	phoneNumber =  models.CharField(max_length = 50, null = True, blank = True)
	email = models.CharField(max_length = 255, null = True, blank = True)
	knownFromDate = models.DateField(max_length = 100, null = True, blank = True)
	idProofCopy = models.FileField(upload_to="static/private/employee/files/reference/proof/%Y/%m/", null=True, blank=True)
	signedLetterCopy = models.FileField(upload_to="static/private/employee/files/reference/letter/%Y/%m/", null=True, blank=True)



class EmployeeReferralDetails(models.Model):
	employeeId = models.ForeignKey(EmployeeMaster)
	referralId = models.ForeignKey(EmployeeMaster, blank=True, null=True, related_name='EmployeeReferralID')
	referralName = models.CharField(max_length = 100, null = True, blank = True, db_index = True)
	referralEmpCode = models.CharField(max_length = 10, null = True, blank = True, db_index = True)