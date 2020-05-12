from django.db import models


class Collection(models.Model):
    coll_name = models.CharField(max_length=255,
                                 blank=False,
                                 help_text='Use "General Collection" if describing all files as one '
                                           'combined entry; otherwise, create a separate entry '
                                           'for each '
                                           'formally named collection or collection '
                                           'with special characteristics, for example "The Nettie '
                                           'Wheeler '
                                           'Artist Files on Native American Artists."',
                                 default='General Collection')
    coll_description = models.TextField(max_length=1000,
                                        blank=False,
                                        help_text='Provide a general description of the collection, '
                                                  'including such aspects as history and provenance. Also '
                                                  'use this field for general notes about '
                                                  'the collection.')
    coll_access = models.TextField(max_length=1000,
                                   blank=False,
                                   help_text='Add policies and procedures relating to how '
                                             'researchers '
                                             'access and use the collection.')
    coll_website = models.URLField(max_length=255,
                                   blank=True,
                                   help_text='Add website describing or providing access to the collection.')
    coll_services = models.ManyToManyField(to='CollectionService',
                                           related_name='Collection',
                                           help_text='Add reference services offered. Create a new service '
                                                     'if there is not a fit.',
                                           blank=False)
    coll_cat_system = models.ManyToManyField(to='CollectionCatSystem',
                                             related_name='Collection',
                                             help_text='Add systems used for cataloging artist files '
                                                       'collection. Create a new system if there is '
                                                       'not a fit.',
                                             blank=False)
    coll_size = models.TextField(max_length=1000,
                                 help_text='Provide a statement about the size of the collection, '
                                           'including growth rate, etc. Use whatever measurement terms are '
                                           'relevant.',
                                 default='',
                                 blank=False)
    coll_spec_format = models.ManyToManyField(to='CollectionSpecialFormat',
                                              related_name='Collection',
                                              help_text='Add special formats contained in the '
                                                        'collection, either analog or digital. Create a new '
                                                        'type if there is not a fit.',
                                              blank=True)
    coll_dig_projects = models.TextField(max_length=1000,
                                         blank=True,
                                         help_text='Describe digital projects, either completed '
                                                   'or planned.')
    coll_dig_access = models.URLField(max_length=255,
                                      blank=True,
                                      help_text='Provide URL for accessing digital collection.')
    # Need to work on way for user to choose a featured image below
    coll_image = models.ForeignKey('CollectionImage',
                                   on_delete=models.CASCADE,
                                   help_text='Upload images showing example material from files '
                                             'and/or storage systems in use.',
                                   blank=True,
                                   null=True)
    coll_subject_name = models.ManyToManyField(to='CollectionSubjectName',
                                               related_name='Collection',
                                               blank=True,
                                               help_text='Add personal and institutional names that '
                                                         'are '
                                                         'subjects of the collection.')
    coll_subject_topic = models.ManyToManyField(to='CollectionSubjectTopic',
                                                related_name='Collection',
                                                blank=True,
                                                help_text='Add topical terms that are the subject focuses '
                                                          'of the files.')
    coll_subject_city = models.ManyToManyField(to='CollectionSubjectCity',
                                               related_name='Collection',
                                               blank=True,
                                               help_text='Add cities that are subject focuses of the files')
    coll_subject_county = models.ManyToManyField(to='CollectionSubjectCounty',
                                                 related_name='Collection',
                                                 blank=True,
                                                 help_text='Add counties that are subject focuses of the '
                                                           'files.')
    coll_subject_state_prov = models.ManyToManyField(to='CollectionSubjectStateProv',
                                                     related_name='Collection',
                                                     blank=True,
                                                     help_text='Add states or provinces that are subject '
                                                               'focuses of the files.')
    coll_subject_country = models.ManyToManyField(to='CollectionSubjectCountry',
                                                  related_name='Collection',
                                                  blank=True,
                                                  help_text='Add countries that are subject focuses of the '
                                                            'files.')
    coll_subject_geo_area = models.ManyToManyField(to='CollectionSubjectGeoArea',
                                                   related_name='Collection',
                                                   blank=True,
                                                   help_text='Add geographic areas, such as West U.S. that '
                                                             'are subject focuses of the files.')

    # Need to develop a way, function, etc, for entering city then automatically filling in higher
    # geographical hierarchies, including zip
    coll_loc_city = models.CharField(max_length=255,
                                     help_text='Important for providing access to collections '
                                               'located in specific cities.',
                                     blank=False)
    coll_loc_state_prov = models.CharField(max_length=255,
                                           help_text='Important for providing access to '
                                                     'collections '
                                                     'located in specific states or provinces.',
                                           blank=False)
    coll_loc_country = models.CharField(max_length=255,
                                        help_text='Important for providing access to collections '
                                                  'located in specific countries.',
                                        blank=False)
    coll_date_created = models.DateField(auto_now_add=True)
    coll_date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return self.coll_name

    class Meta:
        ordering = ['coll_name']


class CollectionImage(models.Model):
    coll_image = models.ImageField(upload_to='collection/images/',
                                   help_text='Upload images showing example material from files '
                                             'and/or storage systems in use.')


class CollectionSpecialFormat(models.Model):
    # Use id.loc.gov
    coll_special_format_thesaurus_choices = [
        ('TGM', 'Thesaurus for Graphic Materials'),
        ('LCGFT', 'LC Genre/Form Terms'),
        ('Wikipedia', 'Wikipedia'),
        ('Other', 'Other')
    ]
    coll_special_format = models.CharField(max_length=100)
    coll_special_format_thesaurus = models.CharField(max_length=10,
                                                     choices=coll_special_format_thesaurus_choices,
                                                     blank=False)
    coll_special_format_url = models.URLField(max_length=255,
                                              help_text='Provide permalink from id.loc.gov or '
                                                        'Wikipedia URL.',
                                              blank=False)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_special_format

    class Meta:
        ordering = ['coll_special_format']


class CollectionCatSystem(models.Model):
    coll_cat_name = models.CharField(max_length=100)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_cat_name

    class Meta:
        ordering = ['coll_cat_name']


class CollectionService(models.Model):
    coll_serv_name = models.CharField(max_length=100)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_serv_name

    class Meta:
        ordering = ['coll_serv_name']


class CollectionSubjectName(models.Model):
    # Use VIAF
    coll_sub_name = models.CharField(max_length=100,
                                     help_text='Use preferred VIAF form of name.')
    coll_sub_name_url = models.URLField(max_length=255,
                                        help_text='Provide VIAF permalink.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_name

    class Meta:
        ordering = ['coll_sub_name']


class CollectionSubjectTopic(models.Model):
    # Use id.loc.gov?
    coll_sub_thesaurus_choices = [
        ('LCSH', 'Library of Congress Subject Headings'),
        ('AAT', 'Art and Architecture Thesaurus'),
    ]
    coll_sub_topic = models.CharField(max_length=100,
                                      blank=False)
    coll_sub_thesaurus = models.CharField(max_length=10,
                                          choices=coll_sub_thesaurus_choices,
                                          blank=False,
                                          default='LCSH')
    coll_sub_topic_url = models.URLField(max_length=255,
                                         help_text='Provide permalink from id.loc.gov or vocab.getty.edu.',
                                         default='')
    description = models.TextField(max_length=500,
                                   blank=True)

    def __str__(self):
        return self.coll_sub_topic

    class Meta:
        ordering = ['coll_sub_topic']


class CollectionSubjectCity(models.Model):
    # use VIAF
    coll_sub_city = models.CharField(max_length=100,
                                     help_text='Use preferred VIAF form of name.')
    coll_sub_city_url = models.URLField(max_length=255,
                                        help_text='Provide VIAF permalink.',
                                        default='')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_city

    class Meta:
        ordering = ['coll_sub_city']


class CollectionSubjectCounty(models.Model):
    # use VIAF
    coll_sub_county = models.CharField(max_length=100,
                                       help_text='Use preferred VIAF form of name.')
    coll_sub_county_url = models.URLField(max_length=255,
                                          help_text='Provide VIAF permalink.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_county

    class Meta:
        ordering = ['coll_sub_county']


class CollectionSubjectStateProv(models.Model):
    # Use VIAF
    coll_sub_state_prov = models.CharField(max_length=100,
                                           help_text='Use preferred VIAF form of name.')
    coll_sub_state_prov_url = models.URLField(max_length=255,
                                              help_text='Provide VIAF permalink.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_state_prov

    class Meta:
        ordering = ['coll_sub_state_prov']


class CollectionSubjectCountry(models.Model):
    # Use VIAF
    coll_sub_country = models.CharField(max_length=100,
                                        help_text='Use preferred VIAF form of name.')
    coll_sub_country_url = models.URLField(max_length=255,
                                           help_text='Provide VIAF permalink.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_country

    class Meta:
        ordering = ['coll_sub_country']


class CollectionSubjectGeoArea(models.Model):
    # use VIAF
    coll_sub_geo_area = models.CharField(max_length=100,
                                         help_text='Use preferred VIAF form of name.')
    coll_sub_geo_area_url = models.URLField(max_length=255,
                                            help_text='Provide VIAF permalink.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_sub_geo_area

    class Meta:
        ordering = ['coll_sub_geo_area']


class CollectionLanguage(models.Model):
    # use id.loc.gov?
    coll_lang = models.CharField(max_length=100,
                                 help_text='Use language term from '
                                           'http://id.loc.gov/vocabulary/languages.html')
    coll_lang_url = models.URLField(max_length=255,
                                    help_text='Provide URI for term from '
                                              'http://id.loc.gov/vocabulary/languages.html')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.coll_lang

    class Meta:
        ordering = ['coll_lang']
