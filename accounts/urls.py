from django.conf.urls import patterns, url
from .views import create_user, profile, prof_edit
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^create_user/$', create_user, name='create_user'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html',}, name='account_login'),
    url(r'^logout/$', logout, {'next_page': 'dashboard'}, name='logout'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^profile/edit/$', prof_edit, name='prof_edit'),
]