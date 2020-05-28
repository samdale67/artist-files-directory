from django.db import models


class Collector(models.Model):
    inst_main_name = models.CharField('Institution Main Name',
                                      max_length=255,
                                      help_text='If an institutional collection, provide main institution '
                                                'name.',
                                      blank=True)
    inst_sub_name = models.CharField('Institution Secondary Name',
                                     max_length=255,
                                     help_text='If an institutional collection, provide name of department, '
                                               'division, etc., responsible for '
                                               'artist files.',
                                     blank=True)
    inst_type = models.ManyToManyField(to='InstitutionType',
                                       verbose_name=u'Institution Types',
                                       related_name='Collector',
                                       blank=True,
                                       help_text='Choose all types that are relevant. Create a new '
                                                 'type if there is not a fit.')
    person_first_name = models.CharField('First Name',
                                         max_length=255,
                                         blank=False,
                                         help_text='If a personal collection, provide first name of '
                                                   'collector. If institution, provide first name of person '
                                                   'filling '
                                                   'out this form.')
    person_last_name = models.CharField('Last Name',
                                        max_length=255,
                                        blank=False,
                                        help_text='If a personal collection, provide last name of '
                                                   'collector. If institution, provide last name of person '
                                                  'filling out this form.')

    person_type = models.ManyToManyField(to='PersonType',
                                         verbose_name=u'Person Types',
                                         related_name='Collector',
                                         blank=True,
                                         help_text='If a collector, choose all types that are '
                                                   'relevant. Create new type if '
                                                   'there is not a fit.')
    email = models.EmailField('Email',
                              max_length=255,
                              help_text='Provide best email for answering questions about artist '
                                        'files. If an institution, prefer general email such as '
                                        '"library@cartermuseum.org"',
                              blank=False)
    telephone = models.CharField('Telephone',
                                 max_length=50,
                                 help_text='Provide best telephone contact for answering questions about '
                                           'artist files.',
                                 blank=True)
    website = models.URLField('Website',
                              max_length=255,
                              help_text='Provide website address related to institution or person '
                                        'responsible for artist files collection, for example, '
                                        '"www.cartermuseum.org/library"',
                              blank=True)
    instagram = models.CharField('Instagram',
                                 max_length=50,
                                 blank=True)
    twitter = models.CharField('Twitter',
                               max_length=50,
                               blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return self.inst_main_name + self.person_last_name

    class Meta:
        verbose_name = 'Collector'
        verbose_name_plural = 'Collectors'
        ordering = ['inst_main_name']


class InstitutionType(models.Model):
    type_name = models.CharField('Institution Type',
                                 max_length=100,
                                 blank=False)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Institution Type'
        verbose_name_plural = 'Institution Types'
        ordering = ['type_name']


class PersonType(models.Model):
    type_name = models.CharField('Person Type',
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
