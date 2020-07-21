from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
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
from .models import CollectionDocument
# from .models import City
# from .models import AFRUser


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'institution_name', 'institution_sub_name', 'person_last_name')

    def institution_name(self, obj):
        return ", ".join([c.inst_main_name for c in obj.collector.all()])

    def institution_sub_name(self, obj):
        return "".join([c.inst_sub_name for c in obj.collector.all()])

    def person_last_name(self, obj):
        return "\n".join([c.person_last_name for c in obj.collector.all()])


class CollectionImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'collection', 'institution_name', 'institution_sub_name',
                    'person_last_name')

    def institution_name(self, obj):
        return ", ".join([c.inst_main_name for c in obj.collection.collector.all()])

    def institution_sub_name(self, obj):
        return "".join([c.inst_sub_name for c in obj.collection.collector.all()])

    def person_last_name(self, obj):
        return "\n".join([c.person_last_name for c in obj.collection.collector.all()])


# class AFRUserInline(admin.StackedInline):
#     model = AFRUser
#     can_delete = False
#     verbose_name = "Institution and User Categories"
#     verbose_name_plural = "Additional Info"
#
#
# class AFRUserAdmin(UserAdmin):
#     inlines = (AFRUserInline,)


admin.site.unregister(User)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(CollectionImage, CollectionImageAdmin)
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
admin.site.register(CollectionDocument)
# admin.site.register(City)