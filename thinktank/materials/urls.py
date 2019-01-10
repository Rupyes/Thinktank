from django.conf.urls import url
from django.views.generic import ListView
from .views import material_view

app_name = 'materials'

urlpatterns = [
    url(r'^$', material_view, name="materials"),
]
