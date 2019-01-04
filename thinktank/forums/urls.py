from django.conf.urls import url
from .views import (
    ForumListView,
    ForumDetailView,
    ForumCreateView,
    ForumUpdateView,
    ForumDeleteView,
    add_comment_to_forum,
    reply_to_comment,
    comment_remove,
    reply_remove,
    CommentUpdateView,
    ReplyUpdateView,
)

app_name = 'forums'

urlpatterns = [
    url(r'^$', ForumListView.as_view(), name='forum_list'),
    url(r'^(?P<pk>\d+)$', ForumDetailView.as_view(), name='forum_detail'),
    url(r'^new/$', ForumCreateView.as_view(), name='create_forum'),
    url(r'^(?P<pk>\d+)/edit/$', ForumUpdateView.as_view(), name='update_forum'),
    url(r'^(?P<pk>\d+)/delete/$', ForumDeleteView.as_view(), name='delete_forum'),
    url(r'^(?P<pk>\d+)/comment/$',
        add_comment_to_forum,
        name="add_comment_to_forum"),
    url(r'^/comment/(?P<pk>\d+)/edit/$',
        CommentUpdateView.as_view(),
        name="comment_update"),
    url(r'^(?P<pk>\d+)/comment/(?P<pk1>\d+)/delete/$',
        comment_remove,
        name="comment_remove"),
    url(r'^(?P<pk>\d+)/comment/(?P<pk1>\d+)/reply/$',
        reply_to_comment,
        name="reply_to_comment"),
    url(r'^/comment//reply/(?P<pk>\d+)/edit/$',
        ReplyUpdateView.as_view(),
        name="reply_update"),
    url(r'^(?P<pk>\d+)/comment/(?P<pk1>\d+)/reply/(?P<pk2>\d+)/delete/$',
        reply_remove,
        name="reply_remove")
    # url(r'^(?P<pk>\d+)/edit/$', BlogUpdateView.as_view(), name='blog_update'),
    # url(r'^(?P<pk>\d+)/delete/$', BlogDeleteView.as_view(),
    #     name='blog_delete'),
]
