from django.conf.urls import url
from .views import (SoftwareCreateView, SoftwareListView,
                    SoftwareDetailView, SoftwareUpdateView, SoftwareDeleteView,)

app_name = "softwares"

urlpatterns = [
    url(r'^create/$', SoftwareCreateView.as_view(), name="create_software"),
    url(r'^$', SoftwareListView.as_view(), name="software_list"),
    url(r'^(?P<pk>\d+)/$', SoftwareDetailView.as_view(), name="software_detail"),
    url(r'^(?P<pk>\d+)/edit/$', SoftwareUpdateView.as_view(), name="software_update"),
    url(r'^(?P<pk>\d+)/delete/$',
        SoftwareDeleteView.as_view(), name="software_delete"),
]
