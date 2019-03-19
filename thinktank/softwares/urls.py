from django.conf.urls import url
from .views import (SoftwareCreateView, SoftwareListView,
                    SoftwareDetailView, SoftwareUpdateView, SoftwareDeleteView,
                    ConfigurationCreateView, ConfigurationListView,
                    ConfigurationDetailView, ConfigurationUpdateView, ConfigurationDeleteView,)

app_name = "softwares"

urlpatterns = [
    url(r'^create/$', SoftwareCreateView.as_view(), name="create_software"),
    url(r'^$', SoftwareListView.as_view(), name="software_list"),
    url(r'^(?P<pk>\d+)/$', SoftwareDetailView.as_view(), name="software_detail"),
    url(r'^(?P<pk>\d+)/edit/$', SoftwareUpdateView.as_view(), name="software_update"),
    url(r'^(?P<pk>\d+)/delete/$',
        SoftwareDeleteView.as_view(), name="software_delete"),
    url(r'^confiuration/create/$', ConfigurationCreateView.as_view(),
        name="create_configuration"),
    url(r'^confiuration/$', ConfigurationListView.as_view(),
        name="configuration_list"),
    url(r'^confiuration/(?P<pk>\d+)/$',
        ConfigurationDetailView.as_view(), name="configuration_detail"),
    url(r'^confiuration/(?P<pk>\d+)/edit/$',
        ConfigurationUpdateView.as_view(), name="configuration_update"),
    url(r'^confiuration/(?P<pk>\d+)/delete/$',
        ConfigurationDeleteView.as_view(), name="configuration_delete"),
]
