from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Collector
from .models import InstitutionType
from .forms import AddCollectorForm
from collections_app.models import Collection


def browse_collector(request, collector_id):
    collectors = Collector.objects.filter(pk=collector_id).order_by('sort_name', 'inst_sub_name',
                                                                    'inst_sub2_name').prefetch_related(
        'collections')
    template = 'collectors_app/browse_collectors.html'
    context = {'collectors': collectors}
    return render(request, template, context)


def browse_dealers(request):
    collectors = Collector.objects.filter(inst_type=17).prefetch_related('collections')
    template = 'collectors_app/browse_dealers.html'
    context = {'collectors': collectors}
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


def add_collector(request):
    submitted = False
    if request.method == 'POST':
        form = AddCollectorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collections/add_document/?submitted=True')
    else:
        form = AddCollectorForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'collectors_app/add_collector.html', {'form': form, 'submitted':
        submitted})
