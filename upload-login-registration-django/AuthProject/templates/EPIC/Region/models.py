from django.db import models
from django.conf import settings


# Create your models here.

 
class Region(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=10, unique = True)
	description = models.TextField(blank = True, null = True)
	
	addedOn = models.DateTimeField(auto_now = True)
	addedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='RegionAddedBy', null = True, blank = True)
	updatedOn = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	updatedBy = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='RegionUpdatedBy', null = True, blank = True)
	isActive = models.BooleanField(default = True)
	isDeleted = models.BooleanField(default = False)


	def __str__(self):
		return self.code

