from django.urls import path
from .views import CollectionDetailView

urlpatterns = [
    path('<int:pk>/', CollectionDetailView.as_view(), name='collection_details'),
]
