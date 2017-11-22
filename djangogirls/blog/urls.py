from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^login/$', views.UserLoginFormView.as_view(), name= 'login'),
	url(r'^logout/$', views.logout_view, name= 'logout'),
]
