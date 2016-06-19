from django.db import models

class StatusPage(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)
  description = models.CharField(max_length=1000, null=True, blank=True, default=None)

  def __str__(self):
    return self.name
