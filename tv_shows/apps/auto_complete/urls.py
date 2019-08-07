from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/api$', views.users_api),
    url(r'^users/api/json$', views.users_api_json),
    url(r'^users/api/json2$', views.users_api_json_two)
]       
