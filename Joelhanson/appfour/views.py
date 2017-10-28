from django.shortcuts import render
from appfour.forms import UserProfileInfoForm,UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)
from appfour.models import TravelDetails
from appfour.forms import TravelDetailsForm
# Create your views here.



class IndexView(LoginRequiredMixin,CreateView):
	login_url = '/login/' # if this person is not logged in, where should this person go? To login_url
	context_object_name = 'form'
	model = TravelDetails
	fields = ('username','origin','desitination','paxname','amount','created_date')
	template_name = 'appfour/travel_insert.html'

class TravelListView(LoginRequiredMixin,ListView):
	context_object_name = 'form'
	model = TravelDetails
	template_name = 'appfour/travel_list.html'

def register(request):
	registered = False
	if request.method == "POST":
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileInfoForm(data = request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit = False)
			profile.user = user
			print(profile)
			profile.save()
			registered = True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()
		print("Not POST")
	return render(request,'appfour/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
#
# class ReportListView(LoginRequiredMixin,ListView):
# 	login_url = '/login/'
#     # redirect_field_name = 'appfour/repost.html'
# 	template_name = 'appfour/repost.html'
#     model = TravelDetails
