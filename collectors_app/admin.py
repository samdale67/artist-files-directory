from django.contrib import admin
from .models import Collector
from .models import InstitutionType
from .models import PersonType

admin.site.register(Collector)
admin.site.register(InstitutionType)
admin.site.register(PersonType)
