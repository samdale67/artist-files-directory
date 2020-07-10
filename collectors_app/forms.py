from django.forms import ModelForm
from .models import Collector


class CollectorForm(ModelForm):
    required_css_class = 'required'

    # # Remove colons from labels
    # def __init__(self, *args, **kwargs):
    #     kwargs.setdefault('label_suffix', '')
    #     super(AddCollectorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Collector
        fields = '__all__'
        exclude = ['user']
