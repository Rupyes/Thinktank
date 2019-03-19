from django.conf.urls import url
from .views import (SoftwareCreateView, SoftwareListView,
                    SoftwareDetailView, SoftwareUpdateView, SoftwareDeleteView,
                    ConfigurationCreateView, ConfigurationListView,
                    ConfigurationDetailView, ConfigurationUpdateView, ConfigurationDeleteView,
                    WorkingProjectCreateView, WorkingProjectListView,
                    WorkingProjectDetailView, WorkingProjectUpdateView, WorkingProjectDeleteView,
                    TechnologyCreateView, TechnologyListView,
                    TechnologyDetailView, TechnologyUpdateView, TechnologyDeleteView,)

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

    url(r'^workingproject/create/$', WorkingProjectCreateView.as_view(),
        name="create_workingproject"),
    url(r'^workingproject/$', WorkingProjectListView.as_view(),
        name="workingproject_list"),
    url(r'^workingproject/(?P<pk>\d+)/$',
        WorkingProjectDetailView.as_view(), name="workingproject_detail"),
    url(r'^workingproject/(?P<pk>\d+)/edit/$',
        WorkingProjectUpdateView.as_view(), name="workingproject_update"),
    url(r'^workingproject/(?P<pk>\d+)/delete/$',
        WorkingProjectDeleteView.as_view(), name="workingproject_delete"),


    url(r'^technology/create/$', TechnologyCreateView.as_view(),
        name="create_technology"),
    url(r'^technology/$', TechnologyListView.as_view(),
        name="technology_list"),
    url(r'^technology/(?P<pk>\d+)/$',
        TechnologyDetailView.as_view(), name="technology_detail"),
    url(r'^technology/(?P<pk>\d+)/edit/$',
        TechnologyUpdateView.as_view(), name="technology_update"),
    url(r'^technology/(?P<pk>\d+)/delete/$',
        TechnologyDeleteView.as_view(), name="technology_delete"),
]
