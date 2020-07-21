from collectors_app import views
from django.urls import path, re_path


urlpatterns = [
    re_path(r'^(?P<collector_id>[0-9]+)/$', views.browse_collector, name='browse-collector'),
    path('browse/collector_types/', views.collector_types, name='browse-collector-types'),
    path('browse/collector_type/institution/<int:pk>', views.collector_type_institution,
         name='browse-collector-type-institution'),
    path('browse/collector_type/person/<int:pk>', views.collector_type_person,
         name='browse-collector-type-person'),
    path('browse/dealers/', views.browse_dealers, name='browse-dealers'),
    path('add_collector/', views.add_collector, name='add-collector'),
    path('update/<int:pk>', views.update_collector, name='update-collector'),
    path('delete/<int:pk>', views.delete_collector, name='delete-collector'),
    path('person_types/', views.person_types_list, name='pers_types'),
    path('person_type_update/<int:pk>/', views.person_type_update, name='person_type_update'),
    path('person_type_add/', views.person_type_add, name='person_type_add'),
    path('institution_types/', views.institution_types_list, name='institution_types'),
    path('institution_type_update/<int:pk>/', views.institution_type_update,
         name='institution_type_update'),
    path('institution_type_add/', views.institution_type_add, name='institution_type_add'),
]