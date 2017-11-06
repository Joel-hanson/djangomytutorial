from django.db.models import Q


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    RetrieveDestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    )



from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

from accounts.models import EmployeeEntryData,LeaveModel


from .serializers import (
    EmployeeCreateUpdateSerializer,
    EmployeeDetailSerializer,
    EmployeeListSerializer,
    )


class EmployeeCreateAPIView(CreateAPIView):
    queryset = EmployeeEntryData.objects.all()
    serializer_class = EmployeeDetailSerializer
    #permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmployeeDetailAPIView(RetrieveAPIView):
    queryset = EmployeeEntryData.objects.all()
    serializer_class = EmployeeDetailSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    #lookup_url_kwarg = "abc"


class EmployeeUpdateAPIView(RetrieveUpdateAPIView):
    queryset = EmployeeEntryData.objects.all()
    serializer_class = EmployeeDetailSerializer
    lookup_field = "id"
    permission_classes = [AllowAny]
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
        #email send_email



class EmployeeDeleteAPIView(RetrieveDestroyAPIView):
    queryset = EmployeeEntryData.objects.all()
    serializer_class = EmployeeDetailSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeListSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['emp_email', 'emp_code']

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = EmployeeEntryData.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(emp_email__icontains=query)|
                    Q(emp_code__icontains=query)
                    ).distinct()
        return queryset_list



#
#
# class EmployeeLeaveAPIView(CreateAPIView):
#     queryset = LeaveModel.objects.all()
#     serializer_class = EmployeeLeaveSerializer
#     permission_classes = [IsAuthenticated]
#
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
