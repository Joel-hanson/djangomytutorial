from django.db import models
from django.contrib import auth # authorization tools
from django.contrib.auth.models import User,Group
# Create your models here.

class EmployeeEntryData(models.Model):
	emp_email = models.EmailField(max_length=200,unique=True)
	emp_code=models.CharField(max_length=3,unique=True)
	emp_datejoin=models.DateField(null=False)
	emp_report=models.CharField(max_length=200,unique=True)
	emp_role = models.ForeignKey(Group)
	def __str__(self):
		return self.emp_email
	# def get_api_url(self):
	# 	return reverse("employee-api:detail", kwargs={"emp_code": self.emp_code})
class LeaveModel(models.Model):
	YESNO_CHOICES = ((0, 'No'), (1, 'Yes'))
	emp_LeaveUser = models.ForeignKey(User)
	emp_leavedate = models.DateField(null=False,unique=True)
	emp_leavesanction = models.BooleanField()
	def __str__(self):
		return str(self.emp_LeaveUser)
