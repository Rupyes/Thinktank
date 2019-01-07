from django.conf.urls import url
from .views import event_post_view, EventList, EventDetail, EventDelete

app_name = 'events'

urlpatterns = [
    url(r'^new/$', event_post_view, name='post_event'),
    url(r'^$', EventList.as_view(), name='event_list'),
    url(r'(?P<pk>\d+)/$', EventDetail.as_view(), name='event_detail'),
    url(r'(?P<pk>\d+)/delete/$', EventDelete.as_view(), name='event_delete'),
]
