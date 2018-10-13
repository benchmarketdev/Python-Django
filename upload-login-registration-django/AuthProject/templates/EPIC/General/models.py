from django.db import models
from django.conf import settings



# Create your models here.



class CommonInfo(models.Model):
	name = models.CharField(max_length=50)
	code = models.CharField(max_length=10, unique = True)
	description = models.TextField(null = True, blank = True)

	addedOn = models.DateTimeField(auto_now = True)	
	updatedOn = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	
	isActive = models.BooleanField(default = True)
	isDeleted = models.BooleanField(default = False)

	class Meta:
		abstract = True

	def __str__(self):
		return self.code



class Department(CommonInfo):
	addedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='DepartmentAddedBy', null = True, blank = True)
	updatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='DepartmentUpdatedBy', null = True, blank = True)



class Designation(CommonInfo):
	addedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='DesignationAddedBy', null = True, blank = True)
	updatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='DesignationUpdatedBy', null = True, blank = True)



class Band(CommonInfo):
	addedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='BandAddedBy', null = True, blank = True)
	updatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='BandUpdatedBy', null = True, blank = True)



class Role(CommonInfo):
	addedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='RoleAddedBy', null = True, blank = True)
	updatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='RoleUpdatedBy', null = True, blank = True)