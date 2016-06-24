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

def index(request, status_page_id=None):
  """
  Index view for status page
  """
  if status_page_id:
    pk = status_page_id
  else:
    pk = 1

  # Get page details
  context = {}
  context['status_page'] = api_request('pages-detail', kwargs={'pk': pk})

  if 'detail' in context['status_page'] and context['status_page']['detail'] == 'Not found.':
    return render(request, '404.html', status=404)

  # Get components details
  context['components'] = api_request('page-components-list', kwargs={'page_pk': pk})

  return render(request, 'index.html', context)
