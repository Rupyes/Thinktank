from django.conf.urls import url
from django.views.generic import ListView
from .views import material_view, department_wise_material

app_name = 'materials'

urlpatterns = [
    url(r'^$', material_view, name="materials"),
    url(r'^department/$', department_wise_material, name="materials"),
]
