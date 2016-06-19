from django.conf.urls import url, include
from rest_framework_nested import routers
from easystatusapi import views

router = routers.DefaultRouter()
router.register(r'components', views.ComponentViewSet, 'components')
router.register(r'pages', views.StatusPageViewSet, 'pages')

pages_router = routers.NestedSimpleRouter(router, r'pages', lookup='page')
pages_router.register(r'components', views.PageComponentViewSet, base_name='page-components')

urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^', include(pages_router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
