from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'firstapp'


from rest_framework import renderers

employee_list = views.EmployeeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
employee_detail = views.EmployeeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns = format_suffix_patterns([
    url(r'^', employee_list, name='employee_list'),
    url(r'^/(?P<pk>[0-9]+)/$', employee_detail, name='employee_detail'),
])
