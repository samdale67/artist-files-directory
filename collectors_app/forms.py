from django.forms import ModelForm
from .models import Collector, PersonType, InstitutionType


class CollectorForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Collector
        fields = '__all__'
        exclude = ['user']


class PersonTypeForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = PersonType
        fields = '__all__'
        exclude = ['user']


class InstitutionTypeForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = InstitutionType
        fields = '__all__'
        exclude = ['user']
