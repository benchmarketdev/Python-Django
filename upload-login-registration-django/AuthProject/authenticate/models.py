from django.db import models
from django.dispatch import receiver
from django.conf import settings

class Employee(models.Model):

	firstname = models.CharField(max_length=100,default='')
	lastname = models.CharField(max_length=100)
	email = models.EmailField(blank=True, null=True)
	password = models.CharField(max_length=100)
	mobile = models.CharField(max_length=15, blank=True)
