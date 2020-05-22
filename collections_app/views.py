from django.shortcuts import get_object_or_404, render
from .models import Collection
from persons_app.models import Person
from institutions_app.models import Institution

def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    collector_person = Person.objects.select_related('collection').get(pk=collection_id)
    collector_person_type = collector_person.type.all()
    service = collection.service.all()
    cat_system = collection.cat_system.all()
    spec_format = collection.spec_format.all()
    subject_name = collection.subject_name.all()
    subject_topic = collection.subject_topic.all()
    subject_city = collection.subject_city.all()
    template = 'collections_app/collection_detail.html'
    context = {'collector_person': collector_person,
               'collector_person_type': collector_person_type,
               'collection': collection,
               'service': service,
               'cat_system': cat_system,
               'spec_format': spec_format,
               'subject_name': subject_name,
               'subject_topic': subject_topic,
               'subject_city': subject_city}
    return render(request, template, context)


# def collection_detail(request, collection_id):
#     collection = get_object_or_404(Collection, pk=collection_id)
#     person_collection = Person.objects.filter(person__id=collection_id)
#     per_type = person_collection.type.all()
#     service = collection.service.all()
#     cat_system = collection.cat_system.all()
#     spec_format = collection.spec_format.all()
#     subject_name = collection.subject_name.all()
#     subject_topic = collection.subject_topic.all()
#     subject_city = collection.subject_city.all()
#     template = 'collections_app/collection_detail.html'
#     context = {'person_collection': person_collection,
#                'per_type': per_type,
#                'collection': collection,
#                'service': service,
#                'cat_system': cat_system,
#                'spec_format': spec_format,
#                'subject_name': subject_name,
#                'subject_topic': subject_topic,
#                'subject_city': subject_city}
#     return render(request, template, context)
