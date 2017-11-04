from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions,status,mixins
from django.contrib.auth.models import User
from firstapp.models import EmployeeEntryData
from firstapp.serializers import UserSerializer,EmployeeSrializer
from django.http import Http404
from rest_framework.renderers import TemplateHTMLRenderer
from django.shortcuts import get_object_or_404,redirect



class EmployeeViewSet(APIView):
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'firstapp/employee_list.html'
	# permission_classes = (permissions.IsAdminUser,)
	def get(self,request):
		queryset = EmployeeEntryData.object.all()
		return Response({'profile':queryset})
	# def get(self, request, pk):
	# 	profile = get_object_or_404(EmployeeEntryData,pk=pk)
	# 	fields=('id','emp_code','emp_role','emp_password1','emp_password2','emp_datejoin','emp_report')
	# 	serializer = EmployeeSrializer(profile)
	# 	print(serializer)
	# 	print(profile)
	# 	return Response({'serializer':serializer,'profile':profile})
	#
	# def post(self, request,pk):
	# 	profile = get_object_or_404(EmployeeEntryData,pk=pk)
	# 	serializer = EmployeeSrializer(profile, data=request.data)
	# 	if not serializer.is_valid():
	# 		return Response({'serializer': serializer, 'profile': profile})
	# 	serializer.save()
	# 	return redirect('employee/employee.html')
