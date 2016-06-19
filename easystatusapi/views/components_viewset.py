from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from easystatusapi.models import Component
from easystatusapi.serializers import ComponentSerializer, ComponentListSerializer

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response


class ComponentViewSet(viewsets.ModelViewSet):
  """
  Component resource endpoint
  """
  serializer_class = ComponentSerializer

  def get_queryset(self):
    return Component.objects \
                .all()

  def list(self, request, *args, **kwargs):
    queryset = self.get_queryset()
    serializer = ComponentListSerializer(queryset, many=True)
    return Response(serializer.data)

class PageComponentViewSet(viewsets.ReadOnlyModelViewSet):
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
