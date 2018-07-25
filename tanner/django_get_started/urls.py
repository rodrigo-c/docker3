"""
Definition of urls for django_get_started.
"""

from datetime import datetime
from django.conf.urls import url

from app.forms import BootstrapAuthenticationForm

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()
from app import views
from django.contrib.auth.views import login, logout

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^list/$', views.list, name='list'),
    url(r'^login/$',
        login,
        {
            'template_name': 'app/login.html',
            'next_page': '/list/',
        },
        name='login'),
    url(r'^logout$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('^auth/', include('django.contrib.auth.urls')),
    url(r'test/', views.test_login, name='test'),
    url(r'^(?P<slug>[\w]+)/$', views.page, name='page'),
]
