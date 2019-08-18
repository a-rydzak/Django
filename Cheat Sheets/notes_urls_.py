from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^create$', views.create),
    url(r'^create_again$', views.create_again),
    url(r'^html$', views.html),
    url(r'^(?P<number>[1-9]\d*)$', views.show), # match any integer 
    url(r'^(?P<number>[1-9]\d*)/edit$', views.edit), # match any integer to edit
    url(r'^(?P<number>[1-9]\d*)/delete$', views.destroy)
]       


# url(r'^articles/(?P\d+)$', views.show)
# url(r'^articles/(?P\w+)$', views.show_word)
# url(r'^articles/2003/$', views.special_case_2003)
# url(r'^articles/(?P[0-9]{4})$', views.year_archive)
# url(r'^articles/(?P[0-9]{4})/(?P[0-9]{2})$', views.month_archive)
# url(r'^(?P<number>^0*(?:[1-9][0-9]?|100)$)$', views.show) 

from django.conf.urls import url, include
"""first_routes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^first_app/', include('apps.first_app.urls'))
]
