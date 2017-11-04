from rest_framework import serializers
from firstapp.models import EmployeeEntryData
from django.contrib.auth.models import User
from django import forms

class UserSerializer(serializers.ModelSerializer):
	email = serializers.EmailField(
	max_length=100,
	style={'placeholder': 'Email', 'autofocus': True}
	)
	password = serializers.CharField(
	max_length=100,
	style={'input_type': 'password', 'placeholder': 'Password'}
	)
	remember_me = serializers.BooleanField()
	class Meta():
		model = User
		fields = ('email','password','remember_me')

class EmployeeSrializer(serializers.ModelSerializer):
	emp_name = serializers.CharField()
	emp_code = serializers.CharField()
	emp_email = serializers.CharField()
	emp_role =serializers.CharField()
	emp_report=serializers.DateField()
	emp_datejoin=serializers.DateField()
	emp_password1 = serializers.CharField(style={'input_type': 'password'})
	emp_password2 = serializers.CharField(style={'input_type': 'password'})
	class Meta:
		model = EmployeeEntryData
		fields = '__all__'
	# def validate(self,data):
	# 		cleaned_data = super(EmployeeSrializer, self).clean()
	# 		password = cleaned_data.get("emp_password1")
	# 		confirm_password = cleaned_data.get("emp_password2")
	# 		if password != confirm_password:
	# 		 raise forms.ValidationError(
	# 		 "password and confirm_password does not match"
	# 		 )
	# 		return password
