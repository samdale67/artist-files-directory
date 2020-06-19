from django.db import models
from django.urls import reverse


class Collection(models.Model):
    collector = models.ManyToManyField(to='collectors_app.Collector',
                                       related_name='collections',
                                       verbose_name=u'Collector(s)',
                                       blank=False,
                                       help_text='Create or choose a collector responsible for the '
                                                 'artist files collection. A collection can have '
                                                 'multiple owners, for example, in the case of '
                                                 'consortial or collaborative digital projects.')
    consortium = models.BooleanField('Consortial collection?',
                                     blank=True,
                                     help_text='Is this collection a consortial or collaborative '
                                               'collection?')
    name = models.CharField('Collection Name',
                            max_length=255,
                            blank=False,
                            default='General Artist Files Collection',
                            help_text='Use "General Artist Files Collection" if describing collection as one '
                                      'combined entry; otherwise, create a separate entry '
                                      'for each formally named collection or collection '
                                      'with special characteristics, for example "The Nettie '
                                      'Wheeler Artist Files on Native American Artists. Multiple '
                                      'collections allowed and encouraged."')
    description = models.TextField('Description',
                                   max_length=3000,
                                   blank=True,
                                   help_text='Provide a general description of the collection, '
                                             'including such aspects as history and provenance. Also '
                                             'use this field for general notes about '
                                             'the collection.')
    quote = models.TextField('Quote',
                             max_length=500,
                             blank=True,
                             help_text='Provide a quote or tagline for the collection. Quotes '
                                       'get automatically added.')
    quote_attrib = models.CharField('Quote Attribution',
                                    max_length=255,
                                    blank=True,
                                    help_text='Provide the source of quote or tagline if applicable, '
                                              'including name, title, date, publication source, etc.')
    access = models.TextField('Access and Use',
                              max_length=1000,
                              blank=True,
                              help_text='Add policies and procedures relating to how '
                                        'researchers access and use the collection.')
    website = models.URLField('Website',
                              max_length=255,
                              blank=True,
                              help_text='Add website describing or providing access to the collection.')
    service = models.ManyToManyField(to='CollectionService',
                                     related_name='collections',
                                     verbose_name=u'Reference Services',
                                     blank=True,
                                     help_text='Add reference services offered. Create a new service '
                                               'if there is not a fit.')
    cat_system = models.ManyToManyField(to='CollectionCatSystem',
                                        related_name='collections',
                                        verbose_name=u'Cataloging Systems',
                                        blank=True,
                                        help_text='Add systems used for cataloging artist files '
                                                  'collection. Create a new system if there is '
                                                  'not a fit.')
    size = models.TextField('Size',
                            max_length=1000,
                            default='',
                            blank=True,
                            help_text='Provide a statement about the size of the collection, '
                                      'including growth rate, etc. Use whatever measurement terms are '
                                      'relevant.')
    spec_format = models.ManyToManyField(to='CollectionSpecialFormat',
                                         related_name='collections',
                                         verbose_name=u'Special Formats',
                                         blank=True,
                                         help_text='Add special formats contained in the '
                                                   'collection, either analog or digital. Create a new '
                                                   'type if there is not a fit.')
    dig_projects = models.TextField('Digital Projects',
                                    max_length=3000,
                                    blank=True,
                                    help_text='Describe digital projects, either completed '
                                              'or planned, for this collection.')
    dig_access = models.URLField('Digital Project Website',
                                 max_length=255,
                                 blank=True,
                                 help_text='Provide URL for accessing digital collection.')
    subject_name = models.ManyToManyField(to='CollectionSubjectName',
                                          related_name='collections',
                                          verbose_name=u'Subject: Names',
                                          blank=True,
                                          help_text='Add personal and institutional names that '
                                                    'are subjects of the collection.')
    subject_topic = models.ManyToManyField(to='CollectionSubjectTopic',
                                           related_name='collections',
                                           verbose_name=u'Subject: Topics',
                                           blank=True,
                                           help_text='Add topical terms that are the subject focuses '
                                                     'of the files.')
    subject_city = models.ManyToManyField(to='CollectionSubjectCity',
                                          related_name='collections',
                                          verbose_name=u'Subject: Cities',
                                          blank=True,
                                          help_text='Add cities that are subject focuses of the files.')
    subject_county = models.ManyToManyField(to='CollectionSubjectCounty',
                                            related_name='collections',
                                            verbose_name=u'Subject: Counties',
                                            blank=True,
                                            help_text='Add counties that are subject focuses of the '
                                                      'files.')
    subject_state_prov = models.ManyToManyField(to='CollectionSubjectStateProv',
                                                related_name='collections',
                                                verbose_name=u'Subject: States and '
                                                             'Provinces',
                                                blank=True,
                                                help_text='Add states or provinces that are subject '
                                                          'focuses of the files.')
    subject_country = models.ManyToManyField(to='CollectionSubjectCountry',
                                             related_name='collections',
                                             verbose_name=u'Subject: Countries',
                                             blank=True,
                                             help_text='Add countries that are subject focuses of the '
                                                       'files.')
    subject_geo_area = models.ManyToManyField(to='CollectionSubjectGeoArea',
                                              related_name='collections',
                                              verbose_name=u'Subject: Geographic Areas',
                                              blank=True,
                                              help_text='Add geographic areas, such as "West U.S." that '
                                                        'are subject focuses of the files.')

    # Need to develop a way, function, etc, for entering city then automatically filling in higher
    # geographical hierarchies, including zip
    loc_city = models.CharField('Location: City',
                                max_length=255,
                                help_text='Important for providing access to collections located in '
                                          'specific cities.',
                                blank=True)
    loc_state_prov = models.CharField('Location: State/Province',
                                      max_length=255,
                                      help_text='Important for providing access to collections located'
                                                ' in specific states or provinces.',
                                      blank=True)
    loc_country = models.CharField('Location: Country',
                                   max_length=255,
                                   help_text='Important for providing access to collections located in '
                                             'specific countries.',
                                   blank=True)
    notes = models.TextField('Notes',
                             max_length=1000,
                             blank=True,
                             help_text='Use this field for information that does not fit elsewhere.')
    date_created = models.DateField(auto_now_add=True)
    date_saved = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse('collection_detail', args=[str(self.pk)])

    class Meta:
        verbose_name = 'Collection'
        verbose_name_plural = '** Collections'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class CollectionImage(models.Model):
    image = models.ImageField('Add Image',
                              upload_to='collection/images/',
                              help_text='Upload images showing example material from files '
                                        'and/or storage systems in use.')
    image_caption = models.CharField('Image Caption',
                                     max_length=50,
                                     default='', )
    collection = models.ForeignKey('Collection',
                                   related_name='collections',
                                   verbose_name=u'Related Collection',
                                   on_delete=models.CASCADE,
                                   default='',
                                   blank=True, )

    def __str__(self):
        return self.image_caption

    class Meta:
        verbose_name = 'Collection Image'
        verbose_name_plural = 'Collection Images'


class CollectionService(models.Model):
    serv_name = models.CharField('Reference Service',
                                 max_length=100,
                                 blank=False,
                                 help_text='')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.serv_name

    class Meta:
        verbose_name = 'Reference Service'
        verbose_name_plural = 'Reference Services'
        ordering = ['serv_name']


class CollectionCatSystem(models.Model):
    cat_name = models.CharField('Cataloging System',
                                max_length=100,
                                blank=False,
                                help_text='')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.cat_name

    class Meta:
        verbose_name = 'Cataloging System'
        verbose_name_plural = 'Cataloging Systems'
        ordering = ['cat_name']


class CollectionSpecialFormat(models.Model):
    # Use id.loc.gov
    special_format = models.CharField('Special Format',
                                      max_length=100,
                                      blank=False,
                                      help_text='')
    special_format_url = models.URLField('Term Reference',
                                         max_length=255,
                                         help_text='Provide URI from <a '
                                                   'href="http://id.loc.gov/vocabulary'
                                                   '/graphicMaterials.html" '
                                                   'target="_blank">Thesaurus for Graphic '
                                                   'Materials</a>, '
                                                   '<a '
                                                   'href="http://id.loc.gov/authorities/genreForms'
                                                   '.html" '
                                                   'target="_blank">Library of Congress Genre/Form '
                                                   'Terms</a>, '
                                                   '<a href="http://www.wikipedia.org" '
                                                   'target="_blank">Wikipedia</a> URL, '
                                                   'or other URL.',
                                         blank=True)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.special_format

    class Meta:
        verbose_name = 'Special Format'
        verbose_name_plural = 'Special Formats'
        ordering = ['special_format']


class CollectionSubjectName(models.Model):
    # Use VIAF
    sub_name = models.CharField('Subject: Name',
                                max_length=100,
                                blank=False,
                                help_text='Use preferred <a '
                                          'href="http://www.viaf.org" '
                                          'target="_blank">VIAF</a> form '
                                          'of '
                                          'name if available. Remove delimiters and subfields, '
                                          'e.g. "Hughston, '
                                          'Milan R., 1954- "')
    sub_name_url = models.URLField('Form of Name Reference',
                                   max_length=255,
                                   blank=True,
                                   help_text='Provide <a href="http://www.viaf.org" '
                                             'target="_blank">VIAF</a> permalink.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.sub_name

    class Meta:
        verbose_name = 'Subject: Name'
        verbose_name_plural = 'Subject: Names'
        ordering = ['sub_name']


class CollectionSubjectTopic(models.Model):
    # Use id.loc.gov?
    sub_topic = models.CharField('Subject: Topic',
                                 max_length=100,
                                 blank=False,
                                 help_text='Use term from <a '
                                           'href="http://id.loc.gov/authorities/subjects.html" '
                                           'target="_blank">Library of Congress Subject Headings '
                                           '</a> or other authority if available.')
    sub_topic_url = models.URLField('Term Reference',
                                    max_length=255,
                                    help_text='Provide URI to term.',
                                    default='',
                                    blank=True)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.sub_topic

    class Meta:
        verbose_name = 'Subject: Topic'
        verbose_name_plural = 'Subject: Topics'
        ordering = ['sub_topic']


class CollectionSubjectCity(models.Model):
    # use VIAF
    sub_city = models.CharField('Subject: City',
                                max_length=100,
                                blank=False,
                                help_text='Use term from <a '
                                          'href="http://id.loc.gov/authorities/subjects.html" '
                                          'target="_blank">Library of Congress Subject Headings</a> '
                                          'or other authority if available.')
    sub_city_url = models.URLField('Term Reference',
                                   max_length=255,
                                   help_text='Provide URI to term.',
                                   default='',
                                   blank=True)
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.sub_city

    class Meta:
        verbose_name = 'Subject: City'
        verbose_name_plural = 'Subject: Cities'
        ordering = ['sub_city']


class CollectionSubjectCounty(models.Model):
    # use VIAF
    sub_county = models.CharField('Subject: County',
                                  max_length=100,
                                  blank=False,
                                  help_text='Use term from <a '
                                            'href="http://id.loc.gov/authorities/subjects.html" '
                                            'target="_blank">Library of Congress Subject Headings '
                                            '</a> or other authority if available.')
    sub_county_url = models.URLField('Term Reference',
                                     max_length=255,
                                     blank=True,
                                     help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.sub_county

    class Meta:
        verbose_name = 'Subject: County'
        verbose_name_plural = 'Subject: Counties'
        ordering = ['sub_county']


class CollectionSubjectStateProv(models.Model):
    # Use VIAF
    sub_state_prov = models.CharField('Subject: State/Province',
                                      max_length=100,
                                      blank=False,
                                      help_text='Use term from <a '
                                                'href="http://id.loc.gov/authorities/subjects.html'
                                                '" target="_blank">Library of Congress Subject '
                                                'Headings</a> or other authority if available.')
    sub_state_prov_url = models.URLField('Term Reference',
                                         max_length=255,
                                         blank=True,
                                         help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.sub_state_prov

    class Meta:
        verbose_name = 'Subject: State/Province'
        verbose_name_plural = 'Subject: State/Provinces '
        ordering = ['sub_state_prov']


class CollectionSubjectCountry(models.Model):
    # Use VIAF
    sub_country = models.CharField('Subject: Country',
                                   max_length=100,
                                   blank=False,
                                   help_text='Use term from <a '
                                             'href="http://id.loc.gov/authorities/subjects.html" '
                                             'target="_blank">Library of Congress Subject Headings '
                                             '</a> or other authority if available.')
    sub_country_url = models.URLField('Term Reference',
                                      max_length=255,
                                      blank=True,
                                      help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.sub_country

    class Meta:
        verbose_name = 'Subject: Country'
        verbose_name_plural = 'Subject: Countries'
        ordering = ['sub_country']


class CollectionSubjectGeoArea(models.Model):
    # use VIAF
    sub_geo_area = models.CharField('Subject: Geographic Area',
                                    max_length=100,
                                    blank=False,
                                    help_text='Use term from <a '
                                              'href="http://id.loc.gov/authorities/subjects.html" '
                                              'target="_blank">Library of Congress Subject Headings '
                                              '</a> or other authority if available.')
    sub_geo_area_url = models.URLField('Term Reference',
                                       max_length=255,
                                       blank=True,
                                       help_text='Provide URI to term.')
    notes = models.TextField(max_length=500,
                             blank=True)

    def __str__(self):
        return self.sub_geo_area

    class Meta:
        verbose_name = 'Subject: Geographic Area'
        verbose_name_plural = 'Subject: Geographic Areas'
        ordering = ['sub_geo_area']
