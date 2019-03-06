"""thinktank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete,)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('homepage.urls', namespace="homepage")),
    url(r'^account/', include('accounts.urls', namespace="accounts")),
    url(r'^blog/', include('blogs.urls', namespace="blogs")),
    url(r'^forum/', include('forums.urls', namespace="forums")),
    url(r'^event/', include('events.urls', namespace="events")),
    url(r'^material/', include('materials.urls', namespace="materials")),
    url(r'^thanks/',
        TemplateView.as_view(template_name="thinktank/thanks.html"),
        name="thanks"),
    url(r'^reset_password/$', password_reset, name="reset_password"),
    url(r'^reset-password/done/$', password_reset_done, name="password_reset_done"),
    url(r'^reset-password/confirm/$',
        password_reset_confirm, name="password_reset_confirm"),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        password_reset_confirm, name="password_reset_confirm"),
    url(r'^reset-password/complete/$', password_reset_complete,
        name="password_reset_complete"),

]

if settings.DEBUG == True:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
