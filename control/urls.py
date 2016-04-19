from django.conf.urls import url, include
from control import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^writeToDB/$', views.writeToDB, name='writeToDB'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^verify/$', views.verify, name='verify'),
]
