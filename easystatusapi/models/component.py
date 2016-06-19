from django.db import models

from easystatusapi.models.status_page import StatusPage

class Component(models.Model):
  status_page = models.ForeignKey(StatusPage, null=False, blank=False)
  name = models.CharField(max_length=100, null=False, blank=False)
  description = models.CharField(max_length=1000, null=True, blank=True, default=None)

  def __str__(self):
    return "{} [{}]".format(self.name, self.status_page.__str__())
