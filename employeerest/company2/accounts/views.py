# from django.shortcuts import render
# from django.core.urlresolvers import reverse_lazy #Reverse lazy we user to say, if someone is logged in or loggin out, where he should actually go
from django.views.generic import CreateView,TemplateView
#
# from accounts import forms
# # Create your views here.
#
#
# def register(request):
# 	registered = False
# 	if request.method == "POST":
# 		user_form = UserForm(data = request.POST)
# 		profile_form = UserProfileInfoForm(data = request.POST)
# 		if user_form.is_valid() and profile_form.is_valid():
# 			user = user_form.save()
# 			profile = profile_form.save(commit = False)
# 			user.set_password(profile.password)
# 			user.save()
# 			profile.user = user
# 			profile.save()
# 			registered = True
# 		else:
# 			print(user_form.errors,profile_form.errors)
# 	else:
# 		user_form = UserCreateForm()
# 		profile_form = UserProfileInfoForm()
# 		print("Not POST")
# 	return render(request,'accounts/signup.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
# #
# class SignUp(TemplateView):
# 	pass
class TestView():
	pass
