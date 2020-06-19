from django.shortcuts import render
from .models import Collection
from collectors_app.models import Collector
from collections_app.models import CollectionImage
from .models import CollectionSubjectCity


def collection_detail(request, collection_id):
    collection = Collection.objects.prefetch_related('collector').get(pk=collection_id)
    collection_images = CollectionImage.objects.filter(collection_id=collection_id).all()
    template = 'collections_app/collection_detail.html'
    context = {'collection': collection,
               'collection_images': collection_images}
    return render(request, template, context)


def browse_all_collections(request):
    collections = Collection.objects.prefetch_related('collector').all()
    template = 'collections_app/browse_collections.html'
    context = {'collections': collections}
    return render(request, template, context)


def browse_all_dealers(request):
    dealers = Collector.objects.filter(inst_type=17)
    template = 'collections_app/browse_dealers.html'
    context = {'dealers': dealers}
    return render(request, template, context)


def browse_subject_city(request, id):
    subject_city = CollectionSubjectCity.objects.get(pk=id)
    collections = Collection.objects.filter(subject_city=id).prefetch_related('collector').all()
    template = 'collections_app/browse_collections.html'
    context = {'collections': collections,
               'subject_city': subject_city}
    return render(request, template, context)


def browse_location_country(request, id):
    collections = Collection.objects.filter(loc_country='United States').all()
    template = 'collections_app/collection_browse.html'
    context = {'collections': collections}
    return render(request, template, context)
