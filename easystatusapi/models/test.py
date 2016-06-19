from django.db import models

from easystatusapi.models.component import Component

class Test(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  description = models.CharField(max_length=1000, null=True, blank=True, default=None)
  component = models.ForeignKey(Component)
