from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import InstitutionType, PersonType
from .forms import Collector, CollectorForm, PersonTypeForm, InstitutionTypeForm
from collections_app.models import Collection
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Count


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


def collector_types(request):
    institution_types = InstitutionType.objects.annotate(num_collection=Count(
        'Collector__collections')).filter(num_collection__gt=0).order_by('type_name')
    person_types = PersonType.objects.annotate(num_collection=Count('Collector')).filter(
        num_collection__gt=0).order_by('type_name')
    template = 'collectors_app/browse_collector_types.html'
    context = {'institution_types': institution_types,
               'person_types': person_types}

    return render(request, template, context)


def collector_type_institution(request, pk):
    institution_type = InstitutionType.objects.get(id=pk)
    collectors = Collector.objects.filter(inst_type=pk).order_by('sort_name', 'inst_sub_name',
                                                                 'inst_sub2_name').prefetch_related(
        'collections')
    template = 'collectors_app/browse_collector_type_institution.html'
    context = {'institution_type': institution_type,
               'collectors': collectors}
    return render(request, template, context)


def collector_type_person(request, pk):
    person_type = PersonType.objects.get(id=pk)
    collectors = Collector.objects.filter(person_type=pk).order_by('sort_name', 'inst_sub_name',
                                                                 'inst_sub2_name').prefetch_related(
        'collections')
    template = 'collectors_app/browse_collector_type_person.html'
    context = {'person_type': person_type,
               'collectors': collectors}
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


@login_required(login_url=reverse_lazy('login'))
def person_types_list(request):
    types = PersonType.objects.all().order_by('type_name')
    template = 'collectors_app/person_types.html'
    context = {'types': types}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def person_type_update(request, pk):
    type = PersonType.objects.get(pk=pk)
    form = PersonTypeForm(request.POST or None, instance=type)
    template = 'collectors_app/person_type_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collectors/person_types')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def person_type_add(request):
    form = PersonTypeForm(request.POST or None)
    template = 'collectors_app/person_type_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collectors/person_types/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def institution_types_list(request):
    types = InstitutionType.objects.all().order_by('type_name')
    template = 'collectors_app/institution_types.html'
    context = {'types': types}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def institution_type_update(request, pk):
    type = InstitutionType.objects.get(pk=pk)
    form = InstitutionTypeForm(request.POST or None, instance=type)
    template = 'collectors_app/institution_type_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collectors/institution_types')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def institution_type_add(request):
    form = InstitutionTypeForm(request.POST or None)
    template = 'collectors_app/institution_type_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collectors/institution_types/')

    return render(request, template, context)