from django.db.models import Q


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
	RetrieveUpdateAPIView
    )
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from accounts.models import EmployeeEntryData,LeaveModel

from .serializers import (
	EmployeeLeaveSerializer,
	EmployeeLeaveListSerializer,
    )
class EmployeeLeaveAPIView(CreateAPIView):
    queryset = LeaveModel.objects.all()
    serializer_class = EmployeeLeaveSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployeeLeaveListAPIView(ListAPIView):
	queryset = LeaveModel.objects.all()
	serializer_class = EmployeeLeaveListSerializer
	filter_backends= [SearchFilter, OrderingFilter]
	permission_classes = [IsAuthenticated]
	search_fields = ['emp_leavedate']

	def get_queryset(self, *args, **kwargs):
		#queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
		queryset_list = LeaveModel.objects.all() #filter(user=self.request.user)
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
					Q(emp_leavedate__icontains=query)
					).distinct()
		return queryset_list

class EmployeeLeaveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = LeaveModel.objects.all()
    serializer_class = EmployeeLeaveListSerializer
    lookup_field = "id"
    permission_classes = [AllowAny]
