from django.conf.urls import url,include
from . import views
app_name = 'employee'

urlpatterns=[
    url(r'^entry/',views.EmployeeViewSet.as_view(),name='entry'),
]
