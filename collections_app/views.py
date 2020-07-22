from django.db.models import Count
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import User, Collection, CollectionImage, CollectionDocument, CollectionCatSystem, \
    CollectionSubjectCity, CollectionSpecialFormat, CollectionService, CollectionSubjectName, \
    CollectionSubjectTopic, CollectionSubjectCounty, CollectionSubjectStateProv, CollectionSubjectCountry, \
    CollectionSubjectGeoArea
from collectors_app.models import Collector
from .forms import CollectionForm, ImageForm, DocumentForm, CollectionServicesForm, CatalogingSystemForm, \
    SpecialFormatForm, SubjectNamesForm, SubjectTopicForm, SubjectCityForm, SubjectCountyForm, \
    SubjectStateProvForm, SubjectCountryForm, SubjectGeoAreaForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserEdit
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import update_session_auth_hash
from cities_light.models import Country, Region, City


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


def browse_digital_collections(request):
    digital_collections = Collector.objects.order_by('sort_name', 'inst_sub_name',
                                                     'inst_sub2_name').prefetch_related(
        'collections').filter(collections__dig_access__contains='http')
    template = 'collections_app/browse_collections_digital.html'
    context = {'digital_collections': digital_collections}

    return render(request, template, context)


def collection_detail(request, collection_id):
    collection = Collection.objects.prefetch_related('collector').get(pk=collection_id)
    collection_images = CollectionImage.objects.filter(collection_id=collection_id).all().order_by('?')[:5]
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


def locations_list(request):
    cities = City.objects.annotate(num_collection=Count('collection')).filter(num_collection__gt=0).order_by('display_name')
    states_provs = Region.objects.annotate(num_collection=Count('collection')).filter(num_collection__gt=0).order_by('display_name')
    countries = Country.objects.annotate(num_collection=Count('collection')).filter(num_collection__gt=0).order_by('name')
    template = 'collections_app/browse_collections_locations.html'
    context = {'cities': cities,
               'states_provs': states_provs,
               'countries': countries}

    return render(request, template, context)


def location_city_collections(request, pk):
    city = City.objects.get(id=pk)
    collectors_city = Collector.objects.prefetch_related('collections').filter(
        collections__city_id=pk).order_by('sort_name', 'inst_sub_name', 'inst_sub2_name').distinct()
    template = 'collections_app/browse_collections_location_city.html'
    context = {'city': city,
               'collectors_city': collectors_city}

    return render(request, template, context)


def location_state_prov_collections(request, pk):
    state_prov = Region.objects.get(id=pk)
    collectors_state_prov = Collector.objects.prefetch_related('collections').filter(
        collections__state_province_id=pk).order_by('sort_name', 'inst_sub_name', 'inst_sub2_name').distinct()
    template = 'collections_app/browse_collections_location_state_prov.html'
    context = {'state_prov': state_prov,
               'collectors_state_prov': collectors_state_prov}

    return render(request, template, context)


def location_country_collections(request, pk):
    country = Country.objects.get(id=pk)
    collectors_country = Collector.objects.prefetch_related('collections').filter(
        collections__country_id=pk).order_by('sort_name', 'inst_sub_name',
                                                     'inst_sub2_name').distinct()
    template = 'collections_app/browse_collections_location_country.html'
    context = {'country': country,
               'collectors_country': collectors_country}

    return render(request, template, context)


def subjects_list(request):
    names = CollectionSubjectName.objects.annotate(num_collection=Count('collections')).filter(num_collection__gt=0).order_by('sub_name')
    topics = CollectionSubjectTopic.objects.annotate(num_collection=Count('collections')).filter(num_collection__gt=0).order_by('sub_topic')
    cities = CollectionSubjectCity.objects.annotate(num_collection=Count('collections')).filter(num_collection__gt=0).order_by('sub_city')
    counties = CollectionSubjectCounty.objects.annotate(num_collection=Count('collections')).filter(num_collection__gt=0).order_by('sub_county')
    states_provs = CollectionSubjectStateProv.objects.annotate(num_collection=Count('collections')).filter(num_collection__gt=0).order_by('sub_state_prov')
    countries = CollectionSubjectCountry.objects.annotate(num_collection=Count('collections')).filter(num_collection__gt=0).order_by('sub_country')
    geo_areas = CollectionSubjectGeoArea.objects.annotate(num_collection=Count('collections')).filter(num_collection__gt=0).order_by('sub_geo_area')
    template = 'collections_app/browse_collections_subjects.html'
    context = {'names': names,
               'topics': topics,
               'cities': cities,
               'counties': counties,
               'states_provs': states_provs,
               'countries': countries,
               'geo_areas': geo_areas}

    return render(request, template, context)


def subject_name_collections(request, pk):
    sub_name = CollectionSubjectName.objects.get(id=pk)
    collections_sub_name = Collection.objects.filter(subject_name=pk).prefetch_related('collector')
    template = 'collections_app/browse_collections_subject_name.html'
    context = {'sub_name': sub_name,
               'collections_sub_name': collections_sub_name}

    return render(request, template, context)


def subject_topic_collections(request, pk):
    sub_topic = CollectionSubjectTopic.objects.get(id=pk)
    collections_sub_topic = Collection.objects.filter(subject_topic=pk).prefetch_related('collector')
    template = 'collections_app/browse_collections_subject_topic.html'
    context = {'sub_topic': sub_topic,
               'collections_sub_topic': collections_sub_topic}

    return render(request, template, context)


def subject_city_collections(request, pk):
    sub_city = CollectionSubjectCity.objects.get(id=pk)
    collections_sub_city = Collection.objects.filter(subject_city=pk).prefetch_related('collector')
    template = 'collections_app/browse_collections_subject_city.html'
    context = {'sub_city': sub_city,
               'collections_sub_city': collections_sub_city}

    return render(request, template, context)


def subject_county_collections(request, pk):
    sub_county = CollectionSubjectCounty.objects.get(id=pk)
    collections_sub_county = Collection.objects.filter(subject_county=pk).prefetch_related('collector')
    template = 'collections_app/browse_collections_subject_county.html'
    context = {'sub_county': sub_county,
               'collections_sub_county': collections_sub_county}

    return render(request, template, context)


def subject_state_prov_collections(request, pk):
    sub_state_prov = CollectionSubjectStateProv.objects.get(id=pk)
    collections_sub_state_prov = Collection.objects.filter(subject_state_prov=pk).prefetch_related('collector')
    template = 'collections_app/browse_collections_subject_state_prov.html'
    context = {'sub_state_prov': sub_state_prov,
               'collections_sub_state_prov': collections_sub_state_prov}

    return render(request, template, context)


def subject_country_collections(request, pk):
    sub_country = CollectionSubjectCountry.objects.get(id=pk)
    collections_sub_country = Collection.objects.filter(subject_country=pk).prefetch_related(
        'collector')
    template = 'collections_app/browse_collections_subject_country.html'
    context = {'sub_country': sub_country,
               'collections_sub_country': collections_sub_country}

    return render(request, template, context)


def subject_geo_area_collections(request, pk):
    sub_geo_area = CollectionSubjectGeoArea.objects.get(id=pk)
    collections_sub_geo_area = Collection.objects.filter(subject_geo_area=pk).prefetch_related(
        'collector')
    template = 'collections_app/browse_collections_subject_geo_area.html'
    context = {'sub_geo_area': sub_geo_area,
               'collections_sub_geo_area': collections_sub_geo_area}

    return render(request, template, context)


def tech_data_list(request):
    collections_spec_formats = CollectionSpecialFormat.objects.annotate(num_collection=Count(
        'collections')).filter(
        num_collection__gt=0).order_by('special_format')
    collections_cat_systems = CollectionCatSystem.objects.annotate(num_collection=Count(
        'collections')).filter(
        num_collection__gt=0).order_by('cat_name')
    template = 'collections_app/browse_collections_tech_data.html'
    context = {'collections_spec_formats': collections_spec_formats,
               'collections_cat_systems': collections_cat_systems}

    return render(request, template, context)


def spec_format_collections(request, pk):
    spec_format = CollectionSpecialFormat.objects.get(id=pk)
    collections_spec_format = Collection.objects.filter(spec_format=pk).prefetch_related('collector')
    template = 'collections_app/browse_collections_tech_data_spec_format.html'
    context = {'spec_format': spec_format,
               'collections_spec_format': collections_spec_format}

    return render(request, template, context)


def cat_system_collections(request, pk):
    cat_system = CollectionCatSystem.objects.get(id=pk)
    collections_cat_system = Collection.objects.filter(cat_system=pk).prefetch_related('collector')
    template = 'collections_app/browse_collections_tech_data_cat_system.html'
    context = {'cat_system': cat_system,
               'collections_cat_system': collections_cat_system}

    return render(request, template, context)


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
def image_add(request):

    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES)
        form.fields["collection"].queryset = Collection.objects.filter(user=request.user.id)
        if form.is_valid():
            image = form.save(commit=False)
            image.user_id = request.user.id
            image.save()
            form.save()
            return redirect('/user/content')

    else:
        form = ImageForm()
        form.fields["collection"].queryset = Collection.objects.filter(user=request.user.id)
        template = 'collections_app/image_add.html'
        context = {'form': form}

    return render(request, template, context)


# @login_required(login_url=reverse_lazy('login'))
# def reference_service_update(request, pk):
#     service = CollectionService.objects.get(pk=pk)
#     form = CollectionServicesForm(request.POST or None, instance=service)
#     template = 'collections_app/reference_service_update.html'
#     context = {'form': form}
#
#     if form.is_valid():
#         form.save()
#         return redirect('/collections/reference_services/')
#
#     return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def image_update(request, pk):

    image = CollectionImage.objects.get(pk=pk)

    if request.method == 'POST':
        form = ImageForm(request.POST or None, request.FILES, instance=image)
        form.fields["collection"].queryset = Collection.objects.filter(user=request.user.id)
        if form.is_valid():
            form.save()
            return redirect('/user/content')

    else:
        form = ImageForm(instance=image)
        form.fields["collection"].queryset = Collection.objects.filter(user=request.user.id)
        template = 'collections_app/image_update.html'
        context = {'form': form,
                   'image': image}

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def image_delete(request, pk):
    image = CollectionImage.objects.get(pk=pk)
    template = 'collections_app/image_delete.html'
    context = {'image': image}

    if request.method == 'POST':
        image.delete()
        return redirect('/user/content/')

    return render(request, template, context)


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
def user_edit(request):
    if request.method == 'POST':
        form = UserEdit(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/user/content')
    else:
        form = UserEdit(instance=request.user)
        template = 'collections_app/user_update.html'
        context = {'form': form}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/user/content/')
        else:
            return redirect('user/change-password/')
    else:
        form = PasswordChangeForm(user=request.user)
        template = 'collections_app/user_password_change.html'
        context = {'form': form}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def user_content(request):
    collectors = Collector.objects.filter(user_id=request.user.id).order_by('sort_name')
    collector_count = Collector.objects.count()
    collections = Collection.objects.filter(user_id=request.user.id).order_by('name')
    collection_count = Collection.objects.count()
    image_count = CollectionImage.objects.count()
    images = CollectionImage.objects.filter(user=request.user.id)
    document_count = CollectionDocument.objects.count()
    template = 'collections_app/user_content.html'
    context = {'collectors': collectors,
               'collector_count': collector_count,
               'collections': collections,
               'collection_count': collection_count,
               'image_count': image_count,
               'images': images,
               'document_count': document_count}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def reference_services_list(request):
    services = CollectionService.objects.all().order_by('serv_name')
    template = 'collections_app/reference_services.html'
    context = {'services': services}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def reference_service_update(request, pk):
    service = CollectionService.objects.get(pk=pk)
    form = CollectionServicesForm(request.POST or None, instance=service)
    template = 'collections_app/reference_service_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/reference_services/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def reference_service_add(request):
    form = CollectionServicesForm(request.POST or None)
    template = 'collections_app/reference_service_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/reference_services/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def cataloging_systems_list(request):
    systems = CollectionCatSystem.objects.all().order_by('cat_name')
    template = 'collections_app/cataloging_systems.html'
    context = {'systems': systems}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def cataloging_system_update(request, pk):
    system = CollectionCatSystem.objects.get(pk=pk)
    form = CatalogingSystemForm(request.POST or None, instance=system)
    template = 'collections_app/cataloging_system_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/cataloging_systems/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def cataloging_system_add(request):
    form = CatalogingSystemForm(request.POST or None)
    template = 'collections_app/cataloging_system_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/cataloging_systems/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def special_formats_list(request):
    formats = CollectionSpecialFormat.objects.all().order_by('special_format')
    template = 'collections_app/special_formats.html'
    context = {'formats': formats}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def special_format_update(request, pk):
    f0rmat = CollectionSpecialFormat.objects.get(pk=pk)
    form = SpecialFormatForm(request.POST or None, instance=f0rmat)
    template = 'collections_app/special_format_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/special_formats/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def special_format_add(request):
    form = SpecialFormatForm(request.POST or None)
    template = 'collections_app/special_format_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/special_formats/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subjects_names_list(request):
    names = CollectionSubjectName.objects.all().order_by('sub_name')
    template = 'collections_app/subject_names.html'
    context = {'names': names}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_name_update(request, pk):
    name = CollectionSubjectName.objects.get(pk=pk)
    form = SubjectNamesForm(request.POST or None, instance=name)
    template = 'collections_app/subject_name_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_names/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_name_add(request):
    form = SubjectNamesForm(request.POST or None)
    template = 'collections_app/subject_name_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/special_formats/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subjects_topics_list(request):
    topics = CollectionSubjectTopic.objects.all().order_by('sub_topic')
    template = 'collections_app/subject_topics.html'
    context = {'topics': topics}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_topic_update(request, pk):
    name = CollectionSubjectTopic.objects.get(pk=pk)
    form = SubjectTopicForm(request.POST or None, instance=name)
    template = 'collections_app/subject_topic_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_names/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_topic_add(request):
    form = SubjectTopicForm(request.POST or None)
    template = 'collections_app/subject_topic_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/special_formats/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subjects_cities_list(request):
    cities = CollectionSubjectCity.objects.all().order_by('sub_city')
    template = 'collections_app/subject_cities.html'
    context = {'cities': cities}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_city_update(request, pk):
    city = CollectionSubjectCity.objects.get(pk=pk)
    form = SubjectCityForm(request.POST or None, instance=city)
    template = 'collections_app/subject_city_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_cities/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_city_add(request):
    form = SubjectCityForm(request.POST or None)
    template = 'collections_app/subject_city_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_cities/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subjects_counties_list(request):
    counties = CollectionSubjectCounty.objects.all().order_by('sub_county')
    template = 'collections_app/subject_counties.html'
    context = {'counties': counties}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_county_update(request, pk):
    county = CollectionSubjectCounty.objects.get(pk=pk)
    form = SubjectCountyForm(request.POST or None, instance=county)
    template = 'collections_app/subject_county_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_counties/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_county_add(request):
    form = SubjectCountyForm(request.POST or None)
    template = 'collections_app/subject_county_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_counties/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subjects_states_provinces_list(request):
    states = CollectionSubjectStateProv.objects.all().order_by('sub_state_prov')
    template = 'collections_app/subject_states_provinces.html'
    context = {'states': states}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_state_province_update(request, pk):
    state = CollectionSubjectStateProv.objects.get(pk=pk)
    form = SubjectStateProvForm(request.POST or None, instance=state)
    template = 'collections_app/subject_state_province_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_states_provinces/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_state_province_add(request):
    form = SubjectStateProvForm(request.POST or None)
    template = 'collections_app/subject_state_province_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_states_provinces/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_countries_list(request):
    countries = CollectionSubjectCountry.objects.all().order_by('sub_country')
    template = 'collections_app/subject_countries.html'
    context = {'countries': countries}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_country_update(request, pk):
    country = CollectionSubjectCountry.objects.get(pk=pk)
    form = SubjectCountryForm(request.POST or None, instance=country)
    template = 'collections_app/subject_country_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_countries/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_country_add(request):
    form = SubjectCountryForm(request.POST or None)
    template = 'collections_app/subject_country_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_countries/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_geo_areas_list(request):
    areas = CollectionSubjectGeoArea.objects.all().order_by('sub_geo_area')
    template = 'collections_app/subject_geo_areas.html'
    context = {'areas': areas}
    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_geo_area_update(request, pk):
    geo_area = CollectionSubjectGeoArea.objects.get(pk=pk)
    form = SubjectGeoAreaForm(request.POST or None, instance=geo_area)
    template = 'collections_app/subject_geo_area_update.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_geo_areas/')

    return render(request, template, context)


@login_required(login_url=reverse_lazy('login'))
def subject_geo_area_add(request):
    form = SubjectGeoAreaForm(request.POST or None)
    template = 'collections_app/subject_geo_area_add.html'
    context = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('/collections/subject_geo_areas/')

    return render(request, template, context)
