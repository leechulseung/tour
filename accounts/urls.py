from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^joinus/$', views.joinus, name="joinus"),
    url(r'^index/$', views.index ,name="index"),
]