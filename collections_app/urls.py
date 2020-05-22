from django.urls import path
from collections_app import views
from django.conf.urls import url

urlpatterns = [
    url(r'^(?P<collection_id>[0-9]+)/$', views.collection_detail, name='collection_detail'),
]
