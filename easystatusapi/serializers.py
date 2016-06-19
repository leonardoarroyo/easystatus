from easystatusapi.models import StatusPage, Component
from rest_framework import serializers

class ComponentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Component
    fields = ('id', 'name', 'description', 'status_page')

class ComponentListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Component
    fields = ('id', 'name', 'description', 'status_page')

class StatusPageSerializer(serializers.ModelSerializer):
  class Meta:
    model = StatusPage
    fields = ('id', 'name', 'description')

class StatusPageListSerializer(serializers.ModelSerializer):
  class Meta:
    model = StatusPage
    fields = ('id', 'name', 'description')
