from django.shortcuts import render
from django.shortcuts import get_object_or_404

from easystatusapi.models import StatusPage, Component
from easystatusapi.serializers import StatusPageSerializer, StatusPageListSerializer, ComponentSerializer, ComponentListSerializer

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response


class StatusPageViewSet(viewsets.ModelViewSet):
  """
  StatusPage resource endpoint
  """
  serializer_class = StatusPageSerializer

  def get_queryset(self):
    return StatusPage.objects \
                .all()

  def list(self, request, *args, **kwargs):
    queryset = self.get_queryset()

    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = StatusPageListSerializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = StatusPageListSerializer(queryset, many=True)
    return Response(serializer.data)

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

    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = ComponentListSerializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = ComponentListSerializer(queryset, many=True)
    return Response(serializer.data)
