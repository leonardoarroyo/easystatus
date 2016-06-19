from django.shortcuts import render
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient

import requests
import json

def index(request):
  client = APIClient()
  context = {}

  # Load status page
  url = reverse('pages-detail', kwargs={'pk':1})
  response = client.get(url)
  context['status_page'] = json.loads(response.content.decode('utf8'))

  return render(request, 'index.html', context)
