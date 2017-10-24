import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')
import django
django.setup()


# fake

import random
from apptwo.models import UserInfo
from faker import *

fakegen = Faker()
# topic = ['Search','Social','Marketplace','News','Games']
#
# def add_topic():
# 	t = Topic.objects.get_or_create(top_name = random.choice(topic))[0]
# 	t.save()
# 	return t
# def populate(N = 5):
# 	for entry in range(N):
# 		# get data
# 		top = add_topic()
# 		# fake data
# 		fake_url = fakegen.url()
# 		fake_date = fakegen.date()
# 		fake_name = fakegen.company()
# 		# create fake webpage
# 		webpg = Webpage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]
# 		# create fake access
# 		acc_rec = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]

def populate(N = 5):
	for entry in range(N):
		fake_fname = fakegen.first_name()
		fake_lname = fakegen.last_name()
		fake_email = fakegen.email()
		userdata = UserInfo.objects.get_or_create(firstname = fake_fname,lastname = fake_lname,email = fake_email)[0]

if __name__ == '__main__':
	print("populated script")
	populate(20)
	print("populated")
