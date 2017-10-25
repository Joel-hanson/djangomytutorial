from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'appthree/index.html',{"data":"helloworld"})

def other(request):
	return render(request,'appthree/other.html')

def relative(request):
	return render(request,'appthree/relative.html')
