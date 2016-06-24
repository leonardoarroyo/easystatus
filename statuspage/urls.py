from django.conf.urls import url, include

from statuspage import views

urlpatterns = [
    url(r'^', include([
      url(r'^$', views.index),
      url(r'^(?P<status_page_id>\d+)', views.index)
    ])),
]
