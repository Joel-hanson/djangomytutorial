from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# from django.db import models
# from .models import Topic,AccessRecord,Webpage
# from .models import UserInfo
from apptwo.forms import NewUser
# def index(request):
# 	webpage_list = AccessRecord.objects.order_by('date')
# 	date_dict = {"access_record":webpage_list}
# 	return render(request,'apptwo/index.html',context = date_dict)

# def help(request):
# 	my_dict = {'me':"help"}
# 	return render(request,'apptwo/help.html',context = my_dict)
def index(request):
	return HttpResponse("<a href=\"/user\">click here to go to user</a>")

def user(request):
	# webpage_list = UserInfo.objects.order_by('firstname')
	# email_dict = {"access_record":webpage_list}
	form = NewUser()
	if request.method == "POST":
		form = NewUser(request.POST)
		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print("error")
	return render(request,'apptwo/user.html',{'form':form})
