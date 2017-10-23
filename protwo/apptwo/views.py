from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.db import models
def index(request):
	my_dict = {'me':"Hello i am binding index",'shit':"Hello"}
	return render(request,'apptwo/index.html',context = my_dict)

def help(request):
	my_dict = {'me':"help"}
	return render(request,'apptwo/help.html',context = my_dict)
