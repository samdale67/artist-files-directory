from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Collection
from collectors_app.models import Collector
from collections_app.models import CollectionImage
from .models import CollectionSubjectCity
from .forms import AddCollectionForm
from .forms import AddImageForm
from .forms import AddDocumentForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def collection_detail(request, collection_id):
    collection = Collection.objects.prefetch_related('collector').get(pk=collection_id)
    collection_images = CollectionImage.objects.filter(collection_id=collection_id).all()
    template = 'collections_app/collection_detail.html'
    context = {'collection': collection,
               'collection_images': collection_images}
    return render(request, template, context)


def browse_all_collections(request):
    all_collectors = Collector.objects.order_by('sort_name', 'inst_sub_name',
                                                'inst_sub2_name').prefetch_related('collections')
    collection_count = Collection.objects.count()
    template = 'collections_app/browse_collections_all.html'
    context = {'all_collectors': all_collectors,
               'collection_count': collection_count}
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
    collection_images = CollectionImage.objects.select_related('collection').order_by('?')[:15]
    template = 'collections_app/home.html'
    context = {'collection_images': collection_images}
    return render(request, template, context)


def what_are_artist_files(request):
    random_quote = Collection.objects.filter(quote__contains=' ').order_by('?').first()
    template = 'collections_app/what-are-artist-files.html'
    context = {'random_quote': random_quote}
    return render(request, template, context)


# I don't understand why this function has to be here; I think it's called in context_processor.py
def last_database_update(request):
    last_updated_collection_object = Collection.objects.latest('date_saved')
    last_updated_collector_object = Collector.objects.latest('date_saved')
    if last_updated_collection_object.date_saved > last_updated_collector_object.date_saved:
        last_updated_object = last_updated_collection_object
    else:
        last_updated_object = last_updated_collector_object
    template = 'collections_app/header.html'
    context = {'last_updated_object': last_updated_object}
    return render(request, template, context)


def random_collection(request):
    random_collection_object = Collection.objects.order_by('?').first()
    collection = Collection.objects.prefetch_related('collector').get(pk=random_collection_object.id)
    collection_images = CollectionImage.objects.filter(collection_id=random_collection_object.id).all()
    template = 'collections_app/collection_detail.html'
    context = {'collection': collection,
               'collection_images': collection_images}
    return render(request, template, context)


def new_collections(request):
    collections = Collection.objects.prefetch_related('collector').order_by('-date_created')[:8]
    template = 'collections_app/browse_collections_new.html'
    context = {'collections': collections}
    return render(request, template, context)


def browse_consortial_collections(request):
    consortial_collectors = Collector.objects.filter(collections__consortium=True).order_by('sort_name',
                                                                                            'inst_sub_name',
                                                                                            'inst_sub2_name') \
        .prefetch_related('collections')
    template = 'collections_app/browse_collections_consortia.html'
    context = {'consortial_collectors': consortial_collectors}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def add_collection(request):
    submitted = False
    if request.method == 'POST':
        form = AddCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collections/add_collection/?submitted=True')
    else:
        form = AddCollectionForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'collections_app/add_collection.html', {'form': form, 'submitted': submitted})


@login_required(login_url=reverse_lazy('login'))
def add_image(request):
    submitted = False
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collections/add_image/?submitted=True')
    else:
        form = AddImageForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'collections_app/add_image.html', {'form': form, 'submitted': submitted})


@login_required(login_url=reverse_lazy('login'))
def add_document(request):
    submitted = False
    if request.method == 'POST':
        form = AddDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collections/add_document/?submitted=True')
    else:
        form = AddDocumentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'collections_app/add_document.html', {'form': form, 'submitted': submitted})


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)
