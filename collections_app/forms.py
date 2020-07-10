from django.forms import ModelForm
from django import forms
from .models import Collection
from .models import CollectionImage
from .models import CollectionDocument
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CollectionForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Collection
        fields = '__all__'
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


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Especially for password '
                                                                      'reset requests.')
    first_name = forms.CharField(max_length=50, required=False)
    last_name = forms.CharField(max_length=50, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)
