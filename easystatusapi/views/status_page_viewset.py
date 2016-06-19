from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from easystatusapi.models import StatusPage
from easystatusapi.serializers import StatusPageSerializer, StatusPageListSerializer

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
    serializer = StatusPageListSerializer(queryset, many=True)
    return Response(serializer.data)
