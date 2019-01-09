from django.conf.urls import url
from .views import (EventList, EventDetail, EventDelete,
                    event_post_view, event_update_view, delete_photo_of_event, add_photo_on_event,)

app_name = 'events'

urlpatterns = [
    url(r'^new/$', event_post_view, name='post_event'),
    url(r'^$', EventList.as_view(), name='event_list'),
    url(r'(?P<pk>\d+)/$', EventDetail.as_view(), name='event_detail'),
    url(r'(?P<pk>\d+)/delete/$', EventDelete.as_view(), name='event_delete'),
    url(r'(?P<pk>\d+)/edit/$', event_update_view, name='event_edit'),
    url(r'(?P<pk>\d+)/photo/add/$',
        add_photo_on_event, name='add_photo'),
    url(r'(?P<pk>\d+)/photo/(?P<pk1>\d+)/delete$',
        delete_photo_of_event, name='delete_photo'),
]
