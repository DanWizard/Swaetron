from django.db import models
from django.contrib import messages
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class ManageUser(models.Manager):
	def checkEmail(self, postData):
		errors = {}
		echeck = User.objects.filter(email = postData['email'])
		print(echeck)
		for i in echeck:
			if i.email == postData['email']:
				print('****')
				errors ['incorrect'] = 'email has already been used'
				return errors

		if not EMAIL_REGEX.match(postData["email"]):
			errors["incorrect"] ='email is not valid'
		else: 
			errors["correct"] ='thanks for subscribing:)'
		return errors

class User(models.Model):
	email = models.CharField(max_length=255)
	objects = ManageUser()



