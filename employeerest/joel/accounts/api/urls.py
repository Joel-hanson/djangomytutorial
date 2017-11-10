from django.conf.urls import url
from django.contrib import admin

from .views import (
	UserCreateAPIView,
	UserLoginAPIView,
	ActivateAPIView,
	ActivateListAPIView,
	)

urlpatterns = [
	url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
	url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
	url(r'^activate/list/(?P<pk>[\w-]+)/$', ActivateAPIView.as_view(), name='activate'),
	url(r'^activate/list/$', ActivateListAPIView.as_view(), name='activate_list'),
]
