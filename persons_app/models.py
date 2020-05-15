from django.db import models


class Person(models.Model):
    per_last_name = models.CharField('Last Name',
                                     max_length=255,
                                     blank=False)
    per_first_name = models.CharField('First Name',
                                      max_length=255,
                                      blank=False)
    per_email = models.EmailField('Email',
                                  max_length=255,
                                  blank=True)
    per_tel = models.CharField('Telephone',
                               max_length=50,
                               blank=True)
    per_website = models.URLField('Website',
                                  max_length=255,
                                  blank=True)
    per_type = models.ManyToManyField(to='PersonType',
                                      verbose_name=u'Types',
                                      related_name='Person',
                                      help_text='Choose all roles that are relevant. Create new role if '
                                                'there '
                                                'is not a fit.')
    per_collection = models.ForeignKey('collections_app.Collection',
                                       verbose_name=u'Collections',
                                       help_text='Create an artist files collection and provide details. '
                                                 'Use "General Collection" if describing all files as one '
                                                 'combined entry. Create a separate entry for each '
                                                 'formally named collection or collection with special '
                                                 'characteristics, for example \"The Nettie Wheeler Artist '
                                                 'Files on Native American Artists.\" Multiple collections '
                                                 'allowed and encouraged.',
                                       on_delete=models.CASCADE)
    per_date_created = models.DateField(auto_now_add=True)
    per_date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return self.per_last_name + ", " + self.per_first_name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'
        ordering = ['per_last_name']


class PersonType(models.Model):
    type_name = models.CharField('Type',
                                 max_length=100,
                                 blank=False)
    notes = models.TextField(max_length=500,
                             default='',
                             blank=True)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Person Type'
        verbose_name_plural = 'Person Types'
        ordering = ['type_name']
