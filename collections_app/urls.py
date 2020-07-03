from collections_app import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r'^(?P<collection_id>[0-9]+)/$', views.collection_detail, name='collection_detail'),
    path('browse/', views.browse_all_collections, name='browse_collections_all'),
    path('browse/consortia', views.browse_consortial_collections, name='browse_collections_consortia'),
    path('browse/subjects/cities/<id>', views.browse_subject_city, name='browse_subject_city'),
    path('random/', views.random_collection),
    path('new/', views.new_collections),
    path('add_collection/', views.add_collection, name='add_collection'),
    path('add_image/', views.add_image, name='add_image'),
    path('add_document/', views.add_document, name='add_document'),

]