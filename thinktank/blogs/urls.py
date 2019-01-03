from django.conf.urls import url
from .views import (
    BlogListView,
    BlogDetailView,
    CreateBlogView,
    BlogDeleteView,
    BlogUpdateView,
)

app_name = 'blogs'

urlpatterns = [
    url(r'^$', BlogListView.as_view(), name='blog_list'),
    url(r'^(?P<pk>\d+)$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^(?P<pk>\d+)/edit/$', BlogUpdateView.as_view(), name='blog_update'),
    url(r'^new/$', CreateBlogView.as_view(), name='create_blog'),
    url(r'^(?P<pk>\d+)/delete/$', BlogDeleteView.as_view(),
        name='blog_delete'),
]
