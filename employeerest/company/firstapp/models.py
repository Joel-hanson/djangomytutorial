from django.db import models

# Create your models here.
class EmployeeInsertion(models.Model):
	Role = (
    ('Developer', 'Developer'),
    ('Project Head', 'Project Head'),
    ('Team lead', 'Team lead'),
	)
	emp_name=models.CharField(max_length=200,null=False)
	emp_code=models.CharField(max_length=3,unique=True)
	emp_email=models.EmailField(max_length=254)
	emp_password1=models.CharField(max_length=32)
	emp_password2=models.CharField(max_length=32)
	emp_datejoin=models.DateField(null=False)
	emp_role=models.CharField(max_length=200,choices=Role,default='Developer')
	emp_report=models.DateField(null=False)

	def __str__(self):
		return self.emp_code
