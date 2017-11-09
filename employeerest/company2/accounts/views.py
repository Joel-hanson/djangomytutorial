# from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy #Reverse lazy we user to say, if someone is logged in or loggin out, where he should actually go
from django.views.generic import CreateView,TemplateView,ListView
from .models import LeaveModel,ActivateModel,EmployeeEntryData
from django.db.models import Model

class HomePageView(ListView):
	modal = EmployeeEntryData
	template_name='login.html'
	context_object_name = 'contextdata'
	def get_context_data(self, **kwargs):
		if(self.request.user == 'admin'):
			context = super(HomePageView, self).get_context_data(**kwargs)
			context.update({
			'character_universe_list': CharacterUniverse.objects.order_by('name'),
			'more_context': Model.objects.all(),
			})
		else:
			pass
		return context

class Employee_HandlingView(TemplateView):
	template_name='accounts/signupemployee.html'
class Leave_Regimen(TemplateView):
	template_name='leave/leave_regimen.html'
class Leave_Application(TemplateView):
	template_name='leave/leave_application.html'
class Activate_TemplateView(TemplateView):
	template_name='leave/leave_application.html'
