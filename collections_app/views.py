from django.shortcuts import render, get_object_or_404
from .models import Collection, CollectionCatSystem, CollectionImage, CollectionLanguage, \
    CollectionService, CollectionSpecialFormat, CollectionSubjectCity, CollectionSubjectCountry, \
    CollectionSubjectCounty, CollectionSubjectGeoArea, CollectionSubjectName, CollectionSubjectStateProv, \
    CollectionSubjectTopic


def collection_details(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    return render(request, 'collections_app/collection_details.html', {'collection': collection})
