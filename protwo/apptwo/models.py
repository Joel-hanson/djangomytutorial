# import datetime
from django.db import models

# from django.utils.encoding import python_2_unicode_compatible
# from django.utils import timezone

# Create your models here.
# @python_2_unicode_compatible  # only if you need to support Python 2
# class Question(models.Model):
# 	question_text = models.CharField(max_length=200)
# 	pub_date = models.DateTimeField('date published')
# 	def __str__(self):
# 		return self.question_text
# 	def was_published_recently(self):
# 		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# @python_2_unicode_compatible  # only if you need to support Python 2
# class Choice(models.Model):
# 	question = models.ForeignKey(Question, on_delete=models.CASCADE)
# 	choice_text = models.CharField(max_length=200)
# 	votes = models.IntegerField(default=0)
# 	def __str__(self):
# 		return self.choice_text


# class Topic(models.Model):
# 	top_name = models.CharField(max_length=264,unique=True)
#
# 	def __str__(self):
# 		return self.top_name
# class Webpage(models.Model):
# 	topic = models.ForeignKey(Topic)
# 	name = models.CharField(max_length=264,unique = True)
# 	url = models.URLField(unique = True)
#
# 	def __str__(self):
# 		return self.name
#
# class AccessRecord(models.Model):
# 	name = models.ForeignKey(Webpage)
# 	date = models.DateField()
# 	def __str__(self):
# 		return str(self.date)
class UserInfo(models.Model):
	firstname = models.CharField(max_length=264)
	lastname = models.CharField(max_length=264)
	email = models.CharField(max_length=264,unique=True)
	def __str__(self):
		return self.email
#
# from aldjemy.core import get_tables, get_engine
# from sqlalchemy.sql import select
#
# def Session():
# 	from protwo import settings
# 	engine = get_engine(settings.DATABASES.default.engine)
# 	# _Session = sessionmaker(bind=engine)
# 	return engine
# s = Session()
# print(s)
