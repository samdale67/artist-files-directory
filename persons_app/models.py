from django.db import models


class Person(models.Model):
    per_last_name = models.CharField(max_length=255,
                                     blank=False)
    per_first_name = models.CharField(max_length=255,
                                      blank=False)
    per_email = models.EmailField(max_length=255,
                                  blank=True)
    per_tel = models.CharField(max_length=50,
                               blank=True)
    per_website = models.URLField(max_length=255,
                                  blank=True)
    per_type = models.ManyToManyField(to='persons_app.PersonType',
                                      related_name='Person',
                                      help_text='Choose all roles that are relevant. Create new role if '
                                                'there '
                                                'is not a fit.')
    per_collection = models.ForeignKey('collections_app.Collection',
                                       on_delete=models.CASCADE,
                                       help_text="Create an artist files collection and provide details. "
                                                 "Multiple "
                                                 "collections allowed and encouraged. Create a separate "
                                                 "entry for each formally named collection or collection "
                                                 "with special characteristics, for example \"The Nettie "
                                                 "Wheeler Artist Files on Native American Artists.\"")
    per_date_created = models.DateField(auto_now_add=True)
    per_date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return self.per_last_name + ", " + self.per_first_name

    class Meta:
        ordering = ['per_last_name']


class PersonType(models.Model):
    type_name = models.CharField(max_length=100,
                                 blank=False)
    notes = models.TextField(max_length=500,
                             default='',
                             blank=True)

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['type_name']
