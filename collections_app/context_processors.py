from collectors_app.models import Collector
from collections_app.models import Collection


def last_database_update(request):
    last_updated_collection_object = Collection.objects.latest('date_saved')
    last_updated_collector_object = Collector.objects.latest('date_saved')
    if last_updated_collection_object.date_saved > last_updated_collector_object.date_saved:
        last_updated_object = last_updated_collection_object
    else:
        last_updated_object = last_updated_collector_object
    return {'last_updated_object': last_updated_object}
