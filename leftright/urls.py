from django.conf.urls import url

from leftright.views import *

urlpatterns = [
    url(r'^$', GameListView.as_view(), name='index'),
    url(r'^do/$', GameDoView.as_view(), name='do'),
]