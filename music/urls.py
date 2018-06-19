from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'music'


urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/712/favourite/
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]


