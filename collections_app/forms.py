from django.forms import ModelForm
from django import forms
from .models import Collection, CollectionImage, CollectionDocument, CollectionService, CollectionCatSystem, \
    CollectionSpecialFormat, CollectionSubjectCity, CollectionSubjectStateProv, CollectionSubjectCountry, \
    CollectionSubjectGeoArea, CollectionSubjectTopic, CollectionSubjectCounty, CollectionSubjectName
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CollectionForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Collection
        exclude = ['user']


class ImageForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionImage
        fields = '__all__'
        exclude = ['user']


class DocumentForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionDocument
        fields = '__all__'
        exclude = ['user']


class CollectionServicesForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionService
        fields = '__all__'


class CatalogingSystemForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionCatSystem
        fields = '__all__'


class SpecialFormatForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionSpecialFormat
        fields = '__all__'


class SubjectNamesForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionSubjectName
        fields = '__all__'


class SubjectTopicForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionSubjectTopic
        fields = '__all__'


class SubjectCityForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionSubjectCity
        fields = '__all__'


class SubjectCountyForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionSubjectCounty
        fields = '__all__'


class SubjectStateProvForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionSubjectStateProv
        fields = '__all__'


class SubjectCountryForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionSubjectCountry
        fields = '__all__'


class SubjectGeoAreaForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = CollectionSubjectGeoArea
        fields = '__all__'


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Especially for password '
                                                                      'reset requests.')
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)


class UserEdit(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name',)
        # Can't seem to hide Password and "No password set"
        help_text = {'password ': '',}
