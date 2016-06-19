from django.conf.urls import url

from statuspage import views

urlpatterns = [
  url(r'^$', views.index),
]
