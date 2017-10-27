from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView,DetailView
# Create your views here.
# def index(request):
	# return render(request,'advanapp/index.html',{"data":request.GET})

class IndexView(TemplateView):
	template_name = 'advanapp/index.html'


	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['injectme'] = 'BASIC INJECTION!'
		return context

from . import models

class SchoolListView(ListView):
	context_object_name = 'schools'
	model = models.School
	template_name = 'advanapp/school_list.html'
	#school_lst

class SchoolDetailView(DetailView):
	#school
	context_object_name = 'school_test'
	model = models.School
	template_name = 'advanapp/school_details.html'
