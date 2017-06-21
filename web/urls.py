from django.conf.urls import url
from .views import home, project_by_id, contact, save_contact

urlpatterns = [
    url(r'^$', home),
    url(r'^projects/(?P<id>\d+)/$', project_by_id, name='project_by_id'),
    url(r'^contact/$', contact),
    url(r'^contact/save$', save_contact)
]
