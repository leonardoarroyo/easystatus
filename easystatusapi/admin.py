from django.contrib import admin
from django.utils.html import format_html
from django.core.urlresolvers import reverse

from easystatusapi.models import Component, StatusPage, Test

class StatusPageAdmin(admin.ModelAdmin):
  fields = ['id', 'name', 'description']
  list_display = ['name', 'description']
  readonly_fields = ['id']

class ComponentAdmin(admin.ModelAdmin):
  fields = ['id', 'name', 'description', 'status_page']
  list_display = ['id', 'name', 'show_status_page']
  readonly_fields = ['id']

  def show_status_page(self, obj):
    try:
      page_name = obj.status_page.__str__()
      pk = obj.status_page.id
      url = reverse('admin:easystatusapi_statuspage_change', args=(pk,))
      return format_html("<a href=\"{url}\">{name}</a>", name=page_name, url=url)
    except:
      pass
    return "No status page"

class TestAdmin(admin.ModelAdmin):
  fields = ['id', 'name', 'description', 'component']
  list_display = ['id', 'name', 'show_component']
  readonly_fields = ['id']

  def show_component(self, obj):
    try:
      component_name = obj.component.__str__()
      pk = obj.component.id
      url = reverse('admin:easystatusapi_component_change', args=(pk,))
      return format_html("<a href=\"{url}\">{name}</a>", name=component_name, url=url)
    except:
      pass
    return "No component"

  show_component.short_description = "Component"

admin.site.register(StatusPage, StatusPageAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Test, TestAdmin)
