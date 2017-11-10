from django.conf.urls import url
from django.contrib import admin

from .views import (
    EmployeeCreateAPIView,
    EmployeeDeleteAPIView,
    EmployeeDetailAPIView,
    EmployeeListAPIView,
    EmployeeUpdateAPIView,
    )
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    url(r'^$', EmployeeListAPIView.as_view(), name='list'),
    # url(r'^create/$', EmployeeCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>[\w-]+)/$', EmployeeDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<id>[\w-]+)/edit/$', EmployeeUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<id>[\w-]+)/delete/$', EmployeeDeleteAPIView.as_view(), name='delete'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
