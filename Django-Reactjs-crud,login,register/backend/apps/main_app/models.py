from __future__ import unicode_literals

from django.db import models

import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserValidator(models.Manager):
	def AddUser(self, first_name, last_name, email, password, confirm_password):
		errors = []
		if len(first_name) < 1:
			errors.append("First name cannot be blank!")
		else:	
			for char in first_name:
				if str(char).isdigit():
				 	errors.append("No numbers in the name fields!") 
		if len(last_name) < 1:
			errors.append("Last name cannot be blank!")
		else:	
			for char in last_name:
				if str(char).isdigit():
				 	erros.append("No numbers in the name fields!") 
		if len(password) < 8:
			errors.append("Password must be at least 8 characters long!")
		else:
			secure_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())			
		if not EMAIL_REGEX.match(email):
			errors.append("Please enter a valid email address!")
		else:	
			emails = Users.objects.filter(email=email)
			if len(emails) != 0:	
				errors.append("Email already taken!")
		if password != confirm_password:
			errors.append("Passwords must match!")
		if len(errors) > 0:
			return errors	
		else:
			new_user = Users.objects.create(first_name=first_name, last_name=last_name, email=email, password=secure_password)
			return new_user	
	def login(self, email, password):
		users = Users.objects.filter(email=email)
		if len(users) == 0:
			return "Invalid email!"
		elif bcrypt.checkpw(password.encode(), users[0].password.encode()) == False:
			return "Incorrect password!"
		else:	
			return users[0]	

class Users(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserValidator()
	def __repr__(self):
		return "<Users object: {} {} {}>".format(self.first_name, self.last_name, self.email)

