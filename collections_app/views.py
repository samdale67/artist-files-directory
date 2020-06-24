from django.shortcuts import render
from .models import Collection
from collectors_app.models import Collector
from collections_app.models import CollectionImage
from collectors_app.models import InstitutionType
from .models import CollectionSubjectCity


def collection_detail(request, collection_id):
    collection = Collection.objects.prefetch_related('collector').get(pk=collection_id)
    collection_images = CollectionImage.objects.filter(collection_id=collection_id).all()
    template = 'collections_app/collection_detail.html'
    context = {'collection': collection,
               'collection_images': collection_images}
    return render(request, template, context)


def browse_all_collections(request):
    collections = Collection.objects.prefetch_related('collector').order_by('collector__sort_name',
                                                                            'collector__inst_sub_name',
                                                                            'collector__inst_sub2_name',
                                                                            'name').all()
    template = 'collections_app/browse_collections.html'
    context = {'collections': collections}
    return render(request, template, context)


def randomized_collection_object(request):
    random_collection_object = Collection.objects.filter(name__isnull=False).order_by('?').first()
    template = 'collections_app/navigation.html'
    context = {'random_collection_object': random_collection_object}
    return render(request, template, context)


def browse_all_dealers(request):
    dealers = Collector.objects.filter(inst_type=17)
    template = 'collections_app/browse_dealers.html'
    context = {'dealers': dealers}
    return render(request, template, context)


def browse_collector(request, collector_id):
    collections = Collection.objects.prefetch_related('collector').filter(
        collector__id=collector_id).order_by(
        'collector__inst_main_name', 'collector__person_last_name', 'name').all()
    template = 'collectors_app/browse_collectors.html'
    context = {'collections': collections}
    return render(request, template, context)


def browse_institution_type(request, id):
    institution_type = InstitutionType.objects.get(pk=id)
    collections = Collection.objects.prefetch_related('collector').filter(
        collector__inst_type=id).order_by('collector__inst_main_name', 'collector__inst_sub_name',
                                          'name').all()
    template = 'collectors_app/browse_collectors.html'
    context = {'institution_type': institution_type,
               'collections': collections}
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


def home_page(request):
    collection_images = CollectionImage.objects.select_related('collection').order_by('?')
    template = 'collections_app/home.html'
    context = {'collection_images': collection_images}
    return render(request, template, context)


def what_are_artist_files(request):
    random_quote = Collection.objects.filter(quote__contains=' ').order_by('?').first()
    template = 'collections_app/what-are-artist-files.html'
    context = {'random_quote': random_quote}
    return render(request, template, context)


def last_database_update(request):
    last_updated_collection_object = Collection.objects.latest('date_saved')
    last_updated_collector_object = Collector.objects.latest('date_saved')
    if last_updated_collection_object.date_saved > last_updated_collector_object.date_saved:
        last_updated_object = last_updated_collection_object
    else:
        last_updated_object = last_updated_collector_object
    template = 'collections_app/base.html'
    context = {'last_updated_object': last_updated_object}
    return render(request, template, context)


def browse_consortial_collections(request):
    collections = Collection.objects.filter(consortium=True).prefetch_related('collector').order_by(
        'collector__sort_name', 'collector__inst_sub2_name', 'name').all()
    template = 'collections_app/browse_collections.html'
    context = {'collections': collections}
    return render(request, template, context)