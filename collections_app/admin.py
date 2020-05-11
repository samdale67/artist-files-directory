from django.contrib import admin
from .models import Collection
from .models import CollectionCatSystem
from .models import CollectionLanguage
from .models import CollectionService
from .models import CollectionSpecialFormat
from .models import CollectionSubjectCountry
from .models import CollectionSubjectCounty
from .models import CollectionSubjectCity
from .models import CollectionSubjectName
from .models import CollectionSubjectGeoArea
from .models import CollectionSubjectTopic
from .models import CollectionSubjectStateProv


admin.site.register(Collection)
admin.site.register(CollectionCatSystem)
admin.site.register(CollectionLanguage)
admin.site.register(CollectionService)
admin.site.register(CollectionSpecialFormat)
admin.site.register(CollectionSubjectCountry)
admin.site.register(CollectionSubjectCounty)
admin.site.register(CollectionSubjectCity)
admin.site.register(CollectionSubjectName)
admin.site.register(CollectionSubjectGeoArea)
admin.site.register(CollectionSubjectTopic)
admin.site.register(CollectionSubjectStateProv)


