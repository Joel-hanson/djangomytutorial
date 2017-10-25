from django.shortcuts import render
from appfour.forms import UserProfileInfoForm,UserForm
# Create your views here.
def index(request):
	return render(request,'appfour/index.html')

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

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()
		print("Not POST")
	return render(request,'appfour/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
