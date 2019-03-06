from django.conf.urls import url
from django.views.generic import ListView
from .views import (add_material, MaterialDetailView, MaterialDeleteView,
                    add_image, delete_image, add_video, delete_video,
                    add_document, delete_document, delete_link, add_link, add_gatematerial, material_view)

app_name = 'materials'

urlpatterns = [
    url(r'^materials/$', material_view, name="material"),
    url(r'^create/$', add_material, name="add_material"),
    url(r'^gate/create/$', add_gatematerial, name="add_gatematerial"),
    url(r'^(?P<pk>\d+)/$',
        MaterialDetailView.as_view(), name="material_detail"),
    url(r'^(?P<pk>\d+)/delete$',
        MaterialDeleteView.as_view(), name="material_delete"),

    url(r'^(?P<pk>\d+)/document/add/$', add_document, name="add_document"),
    url(r'(?P<pk>\d+)/document/(?P<pk1>\d+)/delete$',
        delete_document, name='delete_document'),

    url(r'^(?P<pk>\d+)/link/add/$', add_link, name="add_link"),
    url(r'(?P<pk>\d+)/link/(?P<pk1>\d+)/delete$',
        delete_link, name='delete_link'),

    url(r'^(?P<pk>\d+)/image/add/$', add_image, name="add_image"),
    url(r'(?P<pk>\d+)/image/(?P<pk1>\d+)/delete$',
        delete_image, name='delete_image'),

    url(r'^(?P<pk>\d+)/video/add/$', add_video, name="add_video"),
    url(r'(?P<pk>\d+)/video/(?P<pk1>\d+)/delete$',
        delete_video, name='delete_video'),
]
