from django.shortcuts import render
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView,FormView)
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePage(LoginRequiredMixin,TemplateView):
	login_url = 'login' # if this person is not logged in, where should this person go? To login_url
	context_object_name = 'form'
	model = TravelDetails
	fields = ('origin','desitination','paxname','amount','created_date')
	template_name = 'firstapp/index.html'
	success_url = 'list'
	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.author = self.request.user
		self.object.save()
		return super().form_valid(form)
