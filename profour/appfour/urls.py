from django.conf.urls import url
from . import views

app_name = 'appfour'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^register/',views.register,name="register"),
	url(r'^(?P<pk>\d+)/$',views.IndexView.as_view(),name='detail'),
	url(r'^list/',views.TravelListView.as_view(),name='list'),


]
