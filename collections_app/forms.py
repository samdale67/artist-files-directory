from django.forms import ModelForm
from django.forms import forms
from .models import Collection
from .models import CollectionImage
from .models import CollectionDocument


class AddCollectionForm(ModelForm):
    required_css_class = 'required'

    # # Remove colons from labels
    # def __init__(self, *args, **kwargs):
    #     kwargs.setdefault('label_suffix', '')
    #     super(AddCollectionForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Collection
        fields = '__all__'


class AddImageForm(ModelForm):
    required_css_class = 'required'

    # # Remove colons from labels
    # def __init__(self, *args, **kwargs):
    #     kwargs.setdefault('label_suffix', '')
    #     super(AddImageForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CollectionImage
        fields = '__all__'


class AddDocumentForm(ModelForm):
    required_css_class = 'required'

    # # Remove colons from labels
    # def __init__(self, *args, **kwargs):
    #     kwargs.setdefault('label_suffix', '')
    #     super(AddDocumentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CollectionDocument
        fields = '__all__'
