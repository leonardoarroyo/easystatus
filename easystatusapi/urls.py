from django.conf.urls import url, include
from rest_framework_nested import routers
from easystatusapi import views

router = routers.DefaultRouter()
router.register(r'pages', views.StatusPageViewSet, base_name='pages')

pages_router = routers.NestedSimpleRouter(router, r'pages', lookup='page')
pages_router.register(r'components', views.ComponentViewSet, base_name='page-components')

components_router = routers.NestedSimpleRouter(pages_router, r'components', lookup='component')
components_router.register(r'tests', views.TestViewSet, base_name='component-tests')

urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^', include(pages_router.urls)),
  url(r'^', include(components_router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
