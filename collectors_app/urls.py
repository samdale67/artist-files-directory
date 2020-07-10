from collectors_app import views
from django.urls import path, re_path


urlpatterns = [
    re_path(r'^(?P<collector_id>[0-9]+)/$', views.browse_collector, name='browse-collector'),
    path('browse/institution_type/<id>', views.browse_institution_type, name='browse-collectors'),
    path('browse/dealers/', views.browse_dealers, name='browse-dealers'),
    path('add_collector/', views.add_collector, name='add-collector'),
    path('update/<int:pk>', views.update_collector, name='update-collector'),
    path('delete/<int:pk>', views.delete_collector, name='delete-collector'),
]