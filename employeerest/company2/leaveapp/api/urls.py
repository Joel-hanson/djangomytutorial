from django.conf.urls import url
from django.contrib import admin

from .views import (
    EmployeeLeaveAPIView,
    EmployeeLeaveListAPIView,
	EmployeeLeaveUpdateAPIView
    )


urlpatterns = [
	url(r'^apply/$', EmployeeLeaveAPIView.as_view(), name='Leave_apply'),
	url(r'^$', EmployeeLeaveListAPIView.as_view(), name='Leave_list'),
	url(r'^(?P<id>[\w-]+)/sanction/', EmployeeLeaveUpdateAPIView.as_view(), name='Leave_sanction'),
]
