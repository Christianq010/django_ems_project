"""myems URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from . import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^employees/(?P<pk>[0-9]+)/profile/$', views.my_profile, name='my_profile'),
    # url(r'^$', views.index),
    # below is for our class based view
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^employees/profile/list/$', views.ProfileListView.as_view(), name='profile_list'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/$', views.ProfileDetailView.as_view(), name='my_profile'),
    url(r'^employees/profile/create/$', views.ProfileCreateView.as_view(), name='profile_create'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/update/$', views.ProfileUpdateView.as_view(), name='my_profile_update'),
    url(r'^employees/(?P<pk>[0-9]+)/profile/delete/$', views.ProfileDeleteView.as_view(), name='my_profile_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()

