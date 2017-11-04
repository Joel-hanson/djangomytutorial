from django.conf.urls import url, include
# from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
#
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

# urlpatterns = [
#     # url(r'^', include(router.urls)),
# 	url(r'^restapp/$',views.snippet_list),
# 	url(r'^restapp/(?P<pk>[0-9]+)/$',views.snippet_detail),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

# from rest_framework.urlpatterns import format_suffix_patterns
# from restapp import views
# urlpatterns = [
#     url(r'^snippets/$', views.SnippetList.as_view()),
#     url(r'^snippets/(?P<pk>[0-9]+)$', views.SnippetDetail.as_view()),
#     # url(r'^user/$', views.UserList.as_view()),
#     # url(r'^user/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),
#     # url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
# 	url(r'^$',views.api_root),
# 	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),name='snippet-list'),
# 	url(r'^snippets/(?P<pk>[0-9]+)/$',views.SnippetDetail.as_view(),name='snippet-detail'),
# 	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',views.SnippetHighlight.as_view(),name='snippet-highlight'),
# 	url(r'^users/$',views.UserList.as_view(),name='user-list'),url(r'^users/(?P<pk>[0-9]+)/$',views.UserDetail.as_view(),name='user-detail'),
#
# 	]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
#
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]
#
#
# from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from restapp import views
#
# # API endpoints
# urlpatterns = format_suffix_patterns([
#     # url(r'^$', views.api_root),
#     url(r'^snippets/$',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#     #     views.SnippetHighlight.as_view(),
#         # name='snippet-highlight'),
#     # url(r'^users/$',
#     #     views.UserList.as_view(),
#     #     name='user-list'),
#     # url(r'^users/(?P<pk>[0-9]+)/$',
#     #     views.UserDetail.as_view(),
#     #     name='user-detail')
# ])
#
# # Login and logout views for the browsable API
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]
#


'''url set for viewset and routers  '''

#
# # from restapp.views import SnippetViewSet, UserViewSet, api_root
# from rest_framework import renderers
#
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ])
