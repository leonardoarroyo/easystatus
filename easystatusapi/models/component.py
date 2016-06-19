from django.db import models

from easystatusapi.models.status_page import StatusPage

class Component(models.Model):
  status_page = models.ForeignKey(StatusPage)
  name = models.CharField(max_length=100, null=False, blank=False)
  description = models.CharField(max_length=1000, null=True, blank=True, default=None)
