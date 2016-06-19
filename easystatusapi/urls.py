from django.conf.urls import url, include
from rest_framework import routers
from easystatusapi import views

router = routers.DefaultRouter()
router.register(r'components', views.ComponentViewSet, 'components')
router.register(r'pages', views.StatusPageViewSet, 'pages')

urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
