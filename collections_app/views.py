from django.shortcuts import get_object_or_404, render
from .models import Collection
from collectors_app.models import Collector


def collection_detail(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    collector = get_object_or_404(Collector)
    collector_query = Collection.objects.select_related('collector').filter(id=collection_id).get()
    collector_institution_type = collector.inst_type.all()
    collector_person_type = collector.person_type.all()
    service = collection.service.all()
    cat_system = collection.cat_system.all()
    spec_format = collection.spec_format.all()
    subject_name = collection.subject_name.all()
    subject_topic = collection.subject_topic.all()
    subject_city = collection.subject_city.all()
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
               'subject_city': subject_city}
    return render(request, template, context)
