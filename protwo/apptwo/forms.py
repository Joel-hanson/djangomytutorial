from django import forms
from apptwo.models import UserInfo

class NewUser(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = '__all__'
