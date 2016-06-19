from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from easystatusapi.models import Component
from easystatusapi.serializers import ComponentSerializer, ComponentListSerializer

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

class ComponentViewSet(viewsets.ModelViewSet):
  """
  PageComponent resource endpoint
  """
  serializer_class = ComponentSerializer

  def get_queryset(self, page_pk=None):
    result = Component.objects.all()
    if page_pk:
      result = result.filter(status_page=page_pk)
    return result

  def list(self, request, page_pk=None, *args, **kwargs):
    queryset = self.get_queryset(page_pk=page_pk)
    serializer = ComponentListSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None, page_pk=None, *args, **kwargs):
    try:
      queryset = self.get_queryset(page_pk=page_pk).get(pk=pk)
    except ObjectDoesNotExist:
      return Response({'detail': 'Not found.'}, status=404)

    serializer = self.serializer_class(queryset)
    return Response(serializer.data)

  def create(self, request, page_pk=None, *args, **kwargs):
    data = request.data
    data['status_page'] = page_pk

    serializer = self.serializer_class(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  def destroy(self, request, page_pk=None, pk=None, *args, **kwargs):
    try:
      instance = self.get_queryset(page_pk=page_pk).get(pk=pk)
    except ObjectDoesNotExist:
      return Response({'detail': 'Not found.'}, status=404)

    instance = self.get_object()
    self.perform_destroy(instance)
    return Response(status=status.HTTP_204_NO_CONTENT)

  def update(self, request, page_pk=None, pk=None, *args, **kwargs):
      partial = kwargs.pop('partial', False)

      try:
        instance = self.get_queryset(page_pk=page_pk).get(pk=pk)
      except ObjectDoesNotExist:
        return Response({'detail': 'Not found.'}, status=404)

      serializer = self.get_serializer(instance, data=request.data, partial=partial)
      serializer.is_valid(raise_exception=True)
      self.perform_update(serializer)
      return Response(serializer.data)
