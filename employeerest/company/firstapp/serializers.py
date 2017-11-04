from rest_framework import serializers
from firstapp.models import EmployeeInsertion
from django.contrib.auth.models import User
from django import forms

class EmployeeSrializer(serializers.HyperlinkedModelSerializer):
	emp_password1 = serializers.CharField(style={'input_type': 'password'})
	emp_password2 = serializers.CharField(style={'input_type': 'password'})
	class Meta:
		model = EmployeeInsertion
		fields = ('url','emp_name','emp_email','emp_code','emp_role',
		'emp_password1','emp_password2','emp_datejoin','emp_report')
