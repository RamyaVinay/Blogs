from django.conf.urls import url
#from django.conf import settings
#from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^post/edit/(?P<pk>\d+)/$', views.post_edit, name='post_edit'),
]
