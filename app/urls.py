from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^contact/$', views.contact, name='contact'),
    re_path(r'^post/$', views.post, name='post'),
    re_path(r'^detail/(?P<id>\d+)/$', views.post_details, name='details')

   
]
