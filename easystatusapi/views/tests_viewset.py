from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from easystatusapi.models import Test
from easystatusapi.serializers import TestSerializer
from easystatusapi.serializers import TestListSerializer

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class TestViewSet(viewsets.ModelViewSet):
  """
  Test resource endpoint
  """
  serializer_class = TestSerializer

  def get_queryset(self, component_pk=None, page_pk=None):
    result = Test.objects.all()
    if component_pk:
      result = result.filter(component=component_pk, component__status_page__pk=page_pk)
    return result

  def list(self, request, component_pk=None, page_pk=None, *args, **kwargs):
    queryset = self.get_queryset(component_pk=component_pk, page_pk=page_pk)
    serializer = TestListSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None, component_pk=None, page_pk=None, *args, **kwargs):
    try:
      queryset = self.get_queryset(component_pk=component_pk, page_pk=page_pk).get(pk=pk)
    except ObjectDoesNotExist:
      return Response({'detail': 'Not found.'}, status=404)

    serializer = self.serializer_class(queryset)
    return Response(serializer.data)

  def create(self, request, page_pk=None, component_pk=None, *args, **kwargs):
    data = request.data
    data['component'] = component_pk

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def destroy(self, request, pk=None, component_pk=None, page_pk=None, *args, **kwargs):
    instance = self.get_object()

    try:
      instance = self.get_queryset(component_pk=component_pk, page_pk=page_pk).get(pk=pk)
    except ObjectDoesNotExist:
      return Response({'detail': 'Not found.'}, status=404)

    self.perform_destroy(instance)
    return Response(status=status.HTTP_204_NO_CONTENT)
