from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static
from . import views
urlpatterns = [
	url(r'^help/',views.help,name = 'help'),
	url(r'^$',views.index,name = 'index'),

]
# + static(document_root=settings.STATICFILES_DIRS)
