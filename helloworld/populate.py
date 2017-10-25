import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','protwo.settings')
import django
django.setup()




import random
from first_app.models import Question,Choice
from faker import *

fakegen = Faker()



def populate(N = 5):
	for entry in range(N):
		fake_question_text = fakegen.text()
		fake_pub_date = fakegen.time(pattern="%H:%M:%S", end_datetime=None)
		fake_email = fakegen.email()
		questiondata = Question.objects.get_or_create(question_text = fake_fname,pub_date = fake_pub_date)[0]
		choicedata = Choice.objects.get_or_create(question = questiondata,)
if __name__ == '__main__':
	print("populated script")
	populate(20)
	print("populated")
