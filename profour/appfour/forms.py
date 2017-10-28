from django import forms
from django.contrib.auth.models import User
from appfour.models import UserProfileInfo,TravelDetails
from django.db import models

class UserForm(forms.ModelForm):
	class Meta():
		model = User
		fields = ('first_name','last_name','email','username')
		widgets = {
		# The class here is a CSS class.
		'first_name' : forms.TextInput(attrs={'class':'form-control'}),
		'last_name' : forms.TextInput(attrs={'class':'form-control'}),
		'email' : forms.TextInput(attrs={'class':'form-control'}),
		'username' : forms.TextInput(attrs={'class':'form-control'}),
		}

class UserProfileInfoForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	confirm_password = forms.CharField(widget=forms.PasswordInput)
	class Meta():
		model = UserProfileInfo
		fields = ('password','confirm_password','department',)
		widgets = {
		# The class here is a CSS class.
		# 'password':forms.CharField(attrs={'class':'form-control'}),
		# 'confirm_password':forms.CharField(attrs={'class':'form-control'}),
		'department' : forms.Select(attrs={'class':'form-control'}),
		}
	def clean(self):
		cleaned_data = super(UserProfileInfoForm, self).clean()
		password = cleaned_data.get("password")
		confirm_password = cleaned_data.get("confirm_password")
		if password != confirm_password:
		 raise forms.ValidationError(
		 "password and confirm_password does not match"
		 )

class TravelDetailsForm(forms.ModelForm):
	created_date = forms.DateField(widget=forms.DateInput)
	class Meta():
		model = TravelDetails
		fields =  ('username','origin','desitination','paxname','amount','created_date')
