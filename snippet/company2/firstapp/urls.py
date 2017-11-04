from django.conf.urls import url,include


urlpatterns=[
    url(r'^$', admin.site.urls),
]
