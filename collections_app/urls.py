from collections_app import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^(?P<collection_id>[0-9]+)/$', views.collection_detail, name='collection_detail'),
    path('browse/subjects/cities/<id>', views.browse_subject_city, name='browse_subject_city'),
]