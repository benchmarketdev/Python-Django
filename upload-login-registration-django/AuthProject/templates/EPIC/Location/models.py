from django.db import models
from Region.models import *
from State.models import *


# Create your models here.
 

class Location(models.Model):
	stateId = models.ForeignKey(State, null = True, blank = True)
	
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=10, unique=True)
	address = models.TextField(blank = True, null = True)
	lType = models.CharField(max_length=10, default='DC')		# RO, DC, PPC, 

	addedOn = models.DateTimeField(auto_now = True)
	addedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='LocationAddedBy', null = True, blank = True)
	updatedOn = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	updatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='LocationUpdatedBy', null = True, blank = True)
	isActive = models.BooleanField(default = True)
	isDeleted = models.BooleanField(default = False)



	def __str__(self):
		return self.code
