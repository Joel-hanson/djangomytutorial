from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from firstapp.models import EmployeeInsertion
from firstapp.serializers import EmployeeSrializer

# Create your views here.
def index(request):
	return render(request,'firstapp/index.html')


from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.decorators import detail_route

class EmployeeViewSet(viewsets.ModelViewSet):

	queryset = EmployeeInsertion.objects.all()
	serializer_class = EmployeeSrializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)


"""__________________________________________________"""
