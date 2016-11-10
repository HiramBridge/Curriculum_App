from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    
    url(r'^$', views.PostList.as_view(), name = 'post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name = 'post_detail'),
    url(r'^postnew/$', views.PostCreation.as_view(), name = 'new_post'),
    url(r'^uppost/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view() , name = 'update_post'),
    url(r'^deletepost/(?P<pk>[0-9]+)/$', views.PostDelete.as_view() , name = 'delete_post'),

    

]
