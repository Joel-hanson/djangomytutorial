from django.conf.urls import url
from django.contrib import admin

from .views import (
    EmployeeLeaveAPIView,
    EmployeeLeaveListAPIView,
    )


urlpatterns = [
	url(r'^apply/$', EmployeeLeaveAPIView.as_view(), name='Leave_apply'),
	url(r'^$', EmployeeLeaveListAPIView.as_view(), name='Leave_list'),
]
