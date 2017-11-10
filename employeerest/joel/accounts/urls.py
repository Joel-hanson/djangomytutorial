from django.conf.urls import url
from django.contrib.auth import views as auth_views # Here dJango 1.11 introduces a login in vew and a logout view
from accounts import views #My own views

app_name = 'accounts' #in case I want to use the url templates

urlpatterns = [
    url(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'logout/$', auth_views.LogoutView.as_view(),name='logout'),
	url(r'employee_handling/$',views.Employee_HandlingView.as_view(),name='employee_handling'),
	url(r'leave_regimen/$',views.Leave_Regimen.as_view(),name='leave_regimen'),
	url(r'leave_regimen/$',views.Leave_Regimen.as_view(),name='leave_regimen'),
	url(r'leave_application/$',views.Leave_Application.as_view(),name='leave_application'),
	url(r'activate/(?P<pk>[\w-]+)/$',views.Activate_TemplateView.as_view(),name='activate'),
	]
