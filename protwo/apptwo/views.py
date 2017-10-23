from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
	my_dict = {'me':"Hello i am binding index",'shit':"hello"}
	return render(request,'apptwo/index.html',context = my_dict)
