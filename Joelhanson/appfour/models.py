from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
# Create your models here.

class UserProfileInfo(models.Model):
	user = models.OneToOneField(User)
	TRAVELMATE_SOLUTION = 'Travelmate Solutons'
	TRAVIDUX_TECHNOLOGIES = 'Travidux Technologies'
	department = (
	(TRAVELMATE_SOLUTION, 'Travelmate Solutons'),
	(TRAVIDUX_TECHNOLOGIES, 'Travidux Technologies'),
	)
	department = models.CharField(
	max_length=21,
	choices=department,
	default=TRAVELMATE_SOLUTION,
	)
	password = models.CharField(max_length=30,null=True)
	confirm_password = models.CharField(max_length=30,null=True)
	def __str__(self):
		return self.user.email


class TravelDetails(models.Model):

	author = models.ForeignKey(User,unique=False)
	origin = models.CharField(max_length=200,null=False)
	desitination = models.CharField(max_length=200,null=False)
	paxname = models.CharField(max_length=200,null=True)
	amount = models.FloatField(null=True)
	# details = models.CharField(max_length=200,null=True)
	created_date = models.DateTimeField(default=date.today)

	# def get_absolute_url(self):
    #     return reverse("report", kwargs={'pk':self.pk})

	def __str__(self):
		return str(self.author)
