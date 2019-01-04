from django.conf.urls import url, include
from . import views

app_name = "homepage"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
]
