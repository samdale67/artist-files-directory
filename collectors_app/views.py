from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import Collector
from .models import InstitutionType
from .forms import CollectorForm
from collections_app.models import Collection
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


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


@login_required(login_url=reverse_lazy('login'))
def add_collector(request):
    form = CollectorForm(request.POST or None)
    template = 'collectors_app/add_collector.html'
    context = {"form": form}

    if form.is_valid():
        collector = form.save(commit=False)
        collector.user_id = request.user.id
        collector.save()
        form.save()
        return redirect('/user/content/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def update_collector(request, pk):
    collector = Collector.objects.get(pk=pk)
    form = CollectorForm(request.POST or None, instance=collector)
    template = 'collectors_app/update_collector.html'
    context = {"form": form}

    if form.is_valid():
        form.save()
        return redirect('/user/content/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def delete_collector(request, pk):
    collector = Collector.objects.get(pk=pk)
    # form = CollectionForm(request.POST or None)
    template = 'collectors_app/delete_collector.html'
    context = {"collector": collector}

    if request.method == 'POST':
        collector.delete()
        return redirect('/user/content/')

    return render(request, template, context)


#
# # Old form
# @login_required(login_url=reverse_lazy('login'))
# def add_collector(request):
#     submitted = False
#     if request.method == 'POST':
#         form = CollectorForm(request.POST)
#         if form.is_valid():
#             collector = form.save(commit=False)
#             collector.user_id = request.user.id
#             collector.save()
#             return HttpResponseRedirect('/collections/add_collector/?submitted=True')
#     else:
#         form = CollectorForm()
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'collectors_app/add_collector.html', {'form': form, 'submitted': submitted})

