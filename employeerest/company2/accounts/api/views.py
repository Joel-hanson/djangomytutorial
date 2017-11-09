from django.db.models import Q
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


from rest_framework.filters import (
		SearchFilter,
		OrderingFilter,
	)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView
	)
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from .permissions import IsOwnerOrReadOnly


User = get_user_model()


from .serializers import (
	UserCreateSerializer,
	UserLoginSerializer,
	ActivateSerializer,
	ActivateListSerializer,
	)

from accounts.models import ActivateModel

class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer
	queryset = User.objects.all()
	permission_classes = [AllowAny]



class UserLoginAPIView(APIView):
	permission_classes = [AllowAny]
	serializer_class = UserLoginSerializer
	def post(self, request, *args, **kwargs):
		data = request.data
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			new_data = serializer.data
			return Response(new_data, status=HTTP_200_OK)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class ActivateAPIView(UpdateAPIView):
	serializer_class = ActivateSerializer
	queryset = ActivateModel.objects.all()
	lookup_fields = ('emp_email')
	permission_classes = [AllowAny]

class ActivateListAPIView(ListAPIView):
	serializer_class = ActivateListSerializer
	queryset = ActivateModel.objects.all()
	permission_classes = [AllowAny]
	filter_backends= [SearchFilter, OrderingFilter]
	search_fields = ['emp_email']
	def get_queryset(self, *args, **kwargs):
		queryset_list = ActivateModel.objects.all() #filter(user=self.request.user)
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
								Q(emp_email__icontains=query)
								).distinct()
		return queryset_list
