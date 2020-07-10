from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Collection
from collectors_app.models import Collector
from collections_app.models import CollectionImage, CollectionDocument
from .models import CollectionSubjectCity
from .forms import CollectionForm
from .forms import ImageForm
from .forms import DocumentForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.views.generic.edit import UpdateView


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
    collection_images = CollectionImage.objects.select_related('collection').order_by('?')[:12]
    template = 'collections_app/home.html'
    context = {'collection_images': collection_images}
    return render(request, template, context)


def what_are_artist_files(request):
    random_quote = Collection.objects.filter(quote__contains=' ').order_by('?').first()
    template = 'collections_app/what-are-artist-files.html'
    context = {'random_quote': random_quote}
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
    collections = Collection.objects.prefetch_related('collector').order_by('-date_created')[:10]
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

# OLD FORM
# @login_required(login_url=reverse_lazy('login'))
# def add_collection(request):
#     submitted = False
#     if request.method == 'POST':
#         form = CollectionForm(request.POST)
#         if form.is_valid():
#             collection = form.save(commit=False)
#             collection.user_id = request.user.id
#             collection.save()
#             return HttpResponseRedirect('/collections/add_collection/?submitted=True')
#     else:
#         form = CollectionForm()
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'collections_app/add_collection.html', {'form': form, 'submitted': submitted})


@login_required(login_url=reverse_lazy('login'))
def add_collection(request):
    form = CollectionForm(request.POST or None)
    template = 'collections_app/add_collection.html'
    context = {"form": form}

    if form.is_valid():
        collection = form.save(commit=False)
        collection.user_id = request.user.id
        collection.save()
        form.save()
        return redirect('/user/content/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def update_collection(request, pk):
    collection = Collection.objects.get(pk=pk)
    form = CollectionForm(request.POST or None, instance=collection)
    template = 'collections_app/update_collection.html'
    context = {"form": form}

    if form.is_valid():
        form.save()
        return redirect('/user/content/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def delete_collection(request, pk):
    collection = Collection.objects.get(pk=pk)
    # form = CollectionForm(request.POST or None)
    template = 'collections_app/delete_collection.html'
    context = {"collection": collection}

    if request.method == 'POST':
        collection.delete()
        return redirect('/user/content/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def add_image(request):
    submitted = False
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collections/add_image/?submitted=True')
    else:
        form = ImageForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'collections_app/add_image.html', {'form': form, 'submitted': submitted})


@login_required(login_url=reverse_lazy('login'))
def add_document(request):
    submitted = False
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/collections/add_document/?submitted=True')
    else:
        form = DocumentForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'collections_app/add_document.html', {'form': form, 'submitted': submitted})


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # success_url = reverse_lazy('register-success')
            return redirect('/user/content/')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url=reverse_lazy('login'))
def user_content(request):
    collectors = Collector.objects.filter(user_id=request.user.id).order_by('sort_name')
    collector_count = Collector.objects.count()
    collections = Collection.objects.filter(user_id=request.user.id).order_by('name')
    collection_count = Collection.objects.count()
    image_count = CollectionImage.objects.count()
    document_count = CollectionDocument.objects.count()
    template = 'collections_app/user_content.html'
    context = {'collectors': collectors,
               'collector_count': collector_count,
               'collections': collections,
               'collection_count': collection_count,
               'image_count': image_count,
               'document_count': document_count}
    return render(request, template, context)

