from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,CreateView,UpdateView,DeleteView,TemplateView,ListView,DetailView
from django.core.urlresolvers import reverse_lazy

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
	context_object_name = 'school_detail'
	model = models.School
	template_name = 'advanapp/school_details.html'

class SchoolCreateView(CreateView):
	fields = ('name','principle','location')
	model = models.School

class SchoolUpdateView(UpdateView):
	fields = ('name','principle')
	model = models.School


class SchoolDeleteView(DeleteView):
	model = models.School
	success_url = reverse_lazy("advanapp:list")
