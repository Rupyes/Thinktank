from django.conf.urls import url
from .views import (
    ForumListView,
    ForumDetailView,
    ForumCreateView,
    add_comment_to_forum,
    reply_to_comment,
    reply_to_reply,
)

app_name = 'forums'

urlpatterns = [
    url(r'^$', ForumListView.as_view(), name='forum_list'),
    url(r'^(?P<pk>\d+)$', ForumDetailView.as_view(), name='forum_detail'),
    url(r'^new/$', ForumCreateView.as_view(), name='create_forum'),
    url(r'^(?P<pk>\d+)/comment/$',
        add_comment_to_forum,
        name="add_comment_to_forum"),
    url(r'^(?P<pk>\d+)/comment/(?P<pk1>\d+)/reply/$',
        reply_to_comment,
        name="reply_to_comment"),
    url(r'^(?P<pk>\d+)/comment/(?P<pk1>\d+)/reply/(?P<msg>[a-z]+)/$',
        reply_to_reply,
        name="reply_to_reply"),
    # url(r'^(?P<pk>\d+)/edit/$', BlogUpdateView.as_view(), name='blog_update'),
    # url(r'^(?P<pk>\d+)/delete/$', BlogDeleteView.as_view(),
    #     name='blog_delete'),
]
