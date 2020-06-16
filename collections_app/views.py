from django.shortcuts import render
from .models import Collection
from .models import CollectionSubjectCity


def collection_detail(request, collection_id):
    collection = Collection.objects.prefetch_related('collector').get(pk=collection_id)
    template = 'collections_app/collection_detail.html'
    context = {'collection': collection}
    return render(request, template, context)


def browse_subject_city(request, id):
    subject_city = CollectionSubjectCity.objects.get(pk=id)
    collection = Collection.objects.filter(subject_city=id).prefetch_related('collector')
    template = 'collections_app/collection_browse.html'
    context = {'collection': collection,
               'subject_city': subject_city}
    return render(request, template, context)
