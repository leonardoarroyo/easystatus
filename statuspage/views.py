from django.shortcuts import render
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient

import requests
import json

def api_request(route, kwargs=None):
  """
  Used to make internal request to easystatusapi
  """
  if not kwargs:
    kwargs = {}

  client = APIClient()
  url = reverse(route, kwargs=kwargs)
  response = client.get(url)
  return json.loads(response.content.decode('utf8'))

def index(request):
  """
  Index view for status page
  """
  context = {}
  context['status_page'] = api_request('pages-detail', kwargs={'pk': 1})
  context['components'] = api_request('page-components-list', kwargs={'page_pk': 1})

  print(context)

  return render(request, 'index.html', context)
