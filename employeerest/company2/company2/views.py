from django.views.generic import ListView,TemplateView
from accounts.models import LeaveModel,ActivateModel,EmployeeEntryData
from django.contrib.auth.models import User,Group

class HomePage(ListView):
	template_name = 'index.html'
	context_object_name = 'contextdata'
	queryset = EmployeeEntryData.objects.all()
	def get_context_data(self, **kwargs):
		print(self.request.user)
		context = super(HomePage, self).get_context_data(**kwargs)
		context['leave'] = LeaveModel.objects.all()
		context['activation'] = ActivateModel.objects.all()
		context['employee'] = self.queryset

		
		context['count_ofactivated'] = ActivateModel.objects.filter(active=True).count()
		context['count_ofnonactivated'] = ActivateModel.objects.filter(active=False).count()
		employee_count =  User.objects.all().count()
		context['employee_count'] =employee_count-2
		context['Developer_count']  = EmployeeEntryData.objects.filter(emp_role=1).count()
		context['Teamleader_count'] = EmployeeEntryData.objects.filter(emp_role=2).count()
		context['ProjectManager_count'] =  EmployeeEntryData.objects.filter(emp_role=2).count()
		context['lst_Developers'] = EmployeeEntryData.objects.filter(emp_role = 1).values_list('emp_name',flat=True)
		context['lst_Teamleaders'] = EmployeeEntryData.objects.filter(emp_role = 2).values_list('emp_name',flat=True)
		context['lst_ProjectManagers'] = EmployeeEntryData.objects.filter(emp_role = 3).values_list('emp_name',flat=True)
		name=[]
		data =LeaveModel.objects.all().values_list('emp_LeaveUser__username',flat=True)
		for id in range(len(data)):
			name +=  EmployeeEntryData.objects.filter(emp_email = data[id]).values_list('emp_name',flat=True)
		context['lst_leavenames'] = name
		return context
