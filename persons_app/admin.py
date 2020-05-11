from django.contrib import admin
from .models import Person
from .models import PersonType

admin.site.register(Person)
admin.site.register(PersonType)