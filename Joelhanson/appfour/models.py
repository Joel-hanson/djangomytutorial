from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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
class Places(models.Model):
	destination = models.CharField(max_length=200)
	def __str__(self):
		return self.destination

class TravelDetails(models.Model):
	username = models.ForeignKey('auth.User')
	origin = models.ForeignKey('appfour.Places', related_name='places1')
	desitination = models.ForeignKey('appfour.Places',related_name='places2')
	paxname = models.CharField(max_length=200,null=True)
	amount = models.FloatField(null=True)
	# details = models.CharField(max_length=200,null=True)
	created_date = models.DateTimeField(default=timezone.now)

	# def get_absolute_url(self):
    #     return reverse("report", kwargs={'pk':self.pk})

	def __str__(self):
		return str(self.username)

	def get_absolute_url(self):
			print(self)
			return reverse("appfour:detail", kwargs={'pk':self.pk})
