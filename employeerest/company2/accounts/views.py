# from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy #Reverse lazy we user to say, if someone is logged in or loggin out, where he should actually go
from django.views.generic import CreateView,TemplateView



class HomePageView(TemplateView):
	template_name='login.html'
class Employee_HandlingView(TemplateView):
	template_name='accounts/signupemployee.html'
class Leave_Regimen(TemplateView):
	template_name='leave/leave_regimen.html'
class Leave_Application(TemplateView):
	template_name='leave/leave_application.html'
