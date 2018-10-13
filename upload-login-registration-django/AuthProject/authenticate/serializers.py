from rest_framework import serializers
from models import Employee

class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(required=True)
	password = serializers.CharField(required=True)

	class Meta:
		fields = ['username', 'password']

class Registernewuser(serializers.Serializer):
	firstname = serializers.CharField(required=True)
	lastname = serializers.CharField(required=True)
	email = serializers.EmailField(required=True)
	password = serializers.CharField(required=True)
	mobile = serializers.CharField(required=True)


	class Meta:
		model = Employee
		fields = ['firstname','lastname','email','password','mobile']