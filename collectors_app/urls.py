from collections_app import views
from django.urls import path, re_path


urlpatterns = [
    re_path(r'^(?P<collector_id>[0-9]+)/$', views.browse_collector, name='browse_collector'),
    path('browse/institution_type/<id>', views.browse_institution_type,
         name='browse_collectors'),
    path('browse/subjects/cities/<id>', views.browse_subject_city, name='browse_subject_city'),
    path('browse/dealers/', views.browse_all_dealers, name='browse_dealers'),
]