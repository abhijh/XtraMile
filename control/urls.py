from django.conf.urls import url, include
from control import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
