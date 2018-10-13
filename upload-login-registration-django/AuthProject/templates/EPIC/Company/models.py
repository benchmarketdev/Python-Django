from django.db import models


# Create your models here.


class Company(models.Model):
	name = models.CharField(max_length=255, unique=True)
	totalEmp = models.IntegerField(null = True, blank = True)

	address = models.CharField(max_length=255, null = True, blank = True)
	city = models.CharField(max_length=100, null = True, blank = True)
	state = models.CharField(max_length=100, null = True, blank = True)
	country = models.CharField(max_length=100, null = True, blank = True)
	pin = models.CharField(max_length=20, null = True, blank = True)

	email = models.EmailField(max_length=255, null = True, blank = True)
	website = models.URLField(max_length=255, null = True, blank = True)
	phone = models.CharField(max_length=20, null = True, blank = True)

	createdOn = models.DateTimeField(auto_now = True, null = True, blank = True)
	updatedOn = models.DateTimeField(auto_now_add = True, null = True, blank = True)

	isActive = models.BooleanField(default = True)
	isDeleted = models.BooleanField(default = False)


	def __str__(self):
		return self.name
