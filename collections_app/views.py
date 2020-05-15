from django.views.generic.detail import DetailView
from .models import Collection, CollectionCatSystem, CollectionImage, CollectionLanguage, \
    CollectionService, CollectionSpecialFormat, CollectionSubjectCity, CollectionSubjectCountry, \
    CollectionSubjectCounty, CollectionSubjectGeoArea, CollectionSubjectName, CollectionSubjectStateProv, \
    CollectionSubjectTopic


class CollectionDetailView(DetailView):
    model = Collection
    template_name = 'collections_app/collection_details.html'
