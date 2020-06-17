from django.contrib import admin
from .models import Collection
from .models import CollectionCatSystem
from .models import CollectionService
from .models import CollectionSpecialFormat
from .models import CollectionSubjectCountry
from .models import CollectionSubjectCounty
from .models import CollectionSubjectCity
from .models import CollectionSubjectName
from .models import CollectionSubjectGeoArea
from .models import CollectionSubjectTopic
from .models import CollectionSubjectStateProv
from .models import CollectionImage


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution_name', 'person_last_name')

    def institution_name(self, obj):
        return ", ".join([c.inst_main_name for c in obj.collector.all()])

    def person_last_name(self, obj):
        return "\n".join([c.person_last_name for c in obj.collector.all()])


admin.site.register(Collection, CollectionAdmin)
admin.site.register(CollectionCatSystem)
admin.site.register(CollectionService)
admin.site.register(CollectionSpecialFormat)
admin.site.register(CollectionSubjectCountry)
admin.site.register(CollectionSubjectCounty)
admin.site.register(CollectionSubjectCity)
admin.site.register(CollectionSubjectName)
admin.site.register(CollectionSubjectGeoArea)
admin.site.register(CollectionSubjectTopic)
admin.site.register(CollectionSubjectStateProv)
admin.site.register(CollectionImage)
