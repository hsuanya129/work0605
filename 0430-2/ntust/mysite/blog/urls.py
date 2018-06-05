from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post_page, name='new'),
    url(r'^edit/$', views.edit_page, name='edit'), 
    url(r'^view/$', views.view, name='view'),
    url(r'^save/$', views.save, name='save'), 
    url(r'^update/$', views.update, name='update'), 
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^category/$', views.category, name='category'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), 
]