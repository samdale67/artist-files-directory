from django.contrib import admin
from .models import Collector, InstitutionType, PersonType


class CollectorAdmin(admin.ModelAdmin):
    list_display = ('inst_main_name', 'inst_sub_name', 'person_last_name', 'person_first_name')


admin.site.register(Collector, CollectorAdmin)
admin.site.register(InstitutionType)
admin.site.register(PersonType)
