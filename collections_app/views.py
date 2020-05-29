from django.shortcuts import render
from .models import Collection


def collection_detail(request, collection_id):
    # get a collection object based on collection_id passed through the URL, pk is the primary key for the
    # collection, which is matched with the collection_id pass through the URL
    collection = Collection.objects.get(pk=collection_id)
    # remember, when you access a field that is a foreign key, you automatically get related object! Wow!
    collector = collection.collector
    # you have to make a separate call to bring in inst_type and person_type, and all fields below which are
    # many-to-many fields
    collector_institution_type = collector.inst_type.all()
    collector_person_type = collector.person_type.all()
    service = collection.service.all()
    cat_system = collection.cat_system.all()
    spec_format = collection.spec_format.all()
    subject_name = collection.subject_name.all()
    subject_topic = collection.subject_topic.all()
    subject_city = collection.subject_city.all()
    subject_county = collection.subject_county.all()
    subject_state_prov = collection.subject_state_prov.all()
    subject_country = collection.subject_country.all()
    subject_geo_area = collection.subject_geo_area.all()
    template = 'collections_app/collection_detail.html'
    context = {'collector': collector,
               'collector_institution_type': collector_institution_type,
               'collector_person_type': collector_person_type,
               'collection': collection,
               'service': service,
               'cat_system': cat_system,
               'spec_format': spec_format,
               'subject_name': subject_name,
               'subject_topic': subject_topic,
               'subject_city': subject_city,
               'subject_county': subject_county,
               'subject_state_prov': subject_state_prov,
               'subject_country': subject_country,
               'subject_geo_area': subject_geo_area}
    return render(request, template, context)
