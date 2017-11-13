# from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy #Reverse lazy we user to say, if someone is logged in or loggin out, where he should actually go
from django.views.generic import CreateView,TemplateView,ListView
from .models import LeaveModel,ActivateModel,EmployeeEntryData
from django.db.models import Model

class HomePageView(ListView):
	template_name='login.html'

class Employee_HandlingView(TemplateView):
	template_name='accounts/signupemployee.html'
class Leave_Regimen(TemplateView):
	template_name='leave/leave_regimen.html'
class Leave_Application(TemplateView):
	template_name='leave/leave_application.html'
class Activate_TemplateView(TemplateView):
	template_name='activate/activate.html'
