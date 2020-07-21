from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from cities_light.models import Country, Region, City
from ckeditor.fields import RichTextField


class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    collector = models.ManyToManyField(to='collectors_app.Collector',
                                       related_name='collections',
                                       verbose_name=u'Collector(s)',
                                       blank=False,
                                       help_text='Choose a collector or collectors responsible for the '
                                                 'artist files collection. A collection can have '
                                                 'multiple owners, for example, in the case of '
                                                 'consortial or collaborative digital projects. Hold down '
                                                 '“Control” or “Command” to select more than '
                                                 'one field.')
    consortium = models.BooleanField('Consortial Collection?',
                                     blank=True,
                                     help_text='Check if you have selected more than one collector in the '
                                               'field above.')
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
    country = models.ForeignKey(Country, blank=True, null=True, on_delete=models.CASCADE,
                                verbose_name='Location: Country')
    state_province = models.ForeignKey(Region,
                                       verbose_name='Location: State/Province',
                                       blank=True,
                                       null=True,
                                       on_delete=models.CASCADE)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Location: '
                                                                                                 'City')
    description = RichTextField('Description',
                                max_length=3000,
                                blank=True,
                                help_text='Provide a general description of the collection, '
                                          'including such aspects as history and provenance. Also '
                                          'use this field for general notes about '
                                          'the collection.')
    quote = models.TextField('Quote',
                             max_length=500,
                             blank=True,
                             help_text='Provide a pithy quote or tagline for the collection. This field '
                                       'automatically adds quotes.')
    quote_attrib = models.CharField('Quote Attribution',
                                    max_length=255,
                                    blank=True,
                                    help_text='Provide the source of quote or tagline if applicable, '
                                              'including, at minimum, name, title, institution.')
    access = RichTextField('Access and Use',
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
                                     help_text='Add reference services offered. Hold down “Control” or '
                                               '“Command” to select more than one value.<br /><a '
                                               'href="/collections/reference_services" '
                                               'target="blank">Create or update terms</a>, '
                                               'then return to this page to use.')
    cat_system = models.ManyToManyField(to='CollectionCatSystem',
                                        related_name='collections',
                                        verbose_name=u'Cataloging Systems',
                                        blank=True,
                                        help_text='Add systems used for cataloging artist files '
                                                  'collection. Hold down “Control” or '
                                                  '“Command” to select more than one value.<br /><a '
                                                  'href="/collections/cataloging_systems" '
                                                  'target="blank">Create or update terms</a>, '
                                                  'then return to this page to use.')
    size = RichTextField('Size',
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
                                                   'collection, either analog or digital. Hold down “Control” or '
                                                   '“Command” to select more than one value.<br /><a '
                                                   'href="/collections/special_formats" '
                                                   'target="blank">Create or update terms</a>, '
                                                   'then return to this page to use.')
    dig_projects = RichTextField('Digital Projects',
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
                                                    'are subjects of the collection. Hold down “Control” or '
                                                    '“Command” to select more than one value.<br /><a '
                                                    'href="/collections/subject_names" '
                                                    'target="blank">Create or update terms</a>, then return '
                                                    'to this page to use.')
    subject_topic = models.ManyToManyField(to='CollectionSubjectTopic',
                                           related_name='collections',
                                           verbose_name=u'Subject: Topics',
                                           blank=True,
                                           help_text='Add topical terms that are the subject focuses '
                                                     'of the files. Hold down “Control” or “Command” to '
                                                     'select more than one value.<br /><a '
                                                     'href="/collections/subject_topics" '
                                                     'target="blank">Create or update terms</a>, '
                                                     'then return to this page to use.')
    subject_city = models.ManyToManyField(to='CollectionSubjectCity',
                                          related_name='collections',
                                          verbose_name=u'Subject: Cities',
                                          blank=True,
                                          help_text='Add cities that are subject focuses of the files. Hold '
                                                    'down “Control” or “Command” to select more than one '
                                                    'value.<br /><a href="/collections/subject_cities" '
                                                    'target="blank">Create or update terms</a>, then return '
                                                    'to this page to use.')
    subject_county = models.ManyToManyField(to='CollectionSubjectCounty',
                                            related_name='collections',
                                            verbose_name=u'Subject: Counties',
                                            blank=True,
                                            help_text='Add counties that are subject focuses of the '
                                                      'files. Hold down “Control” or “Command” to select '
                                                      'more than one value.<br /><a '
                                                      'href="/collections/subject_counties" '
                                                      'target="blank">Create or update terms</a>, '
                                                      'then return to this page to use.')
    subject_state_prov = models.ManyToManyField(to='CollectionSubjectStateProv',
                                                related_name='collections',
                                                verbose_name=u'Subject: States and '
                                                             'Provinces',
                                                blank=True,
                                                help_text='Add states or provinces that are subject '
                                                          'focuses of the files. Hold down “Control” or '
                                                          '“Command” to select more than one value.<br /><a '
                                                          'href="/collections/subject_states_provinces" '
                                                          'target="blank">Create or update terms</a>, '
                                                          'then return to this page to use.')
    subject_country = models.ManyToManyField(to='CollectionSubjectCountry',
                                             related_name='collections',
                                             verbose_name=u'Subject: Countries',
                                             blank=True,
                                             help_text='Add countries that are subject focuses of the '
                                                       'files. Hold down “Control” or “Command” to select '
                                                       'more than one value.<br /><a '
                                                       'href="/collections/subject_countries" '
                                                       'target="blank">Create or update terms</a>, '
                                                       'then return to this page to use.')
    subject_geo_area = models.ManyToManyField(to='CollectionSubjectGeoArea',
                                              related_name='collections',
                                              verbose_name=u'Subject: Geographic Areas',
                                              blank=True,
                                              help_text='Add geographic areas, such as "West U.S." that '
                                                        'are subject focuses of the files. Hold down '
                                                        '“Control” or “Command” to select more than one '
                                                        'value.<br /><a '
                                                        'href="/collections/subject_geo_areas" '
                                                        'target="blank">Create or update terms</a>, '
                                                        'then return to this page to use.')
    notes = RichTextField('Notes',
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('Image File',
                              upload_to='collection/images/',
                              help_text='Upload image showing example material from '
                                        'files and/or storage systems in use.<br />It seems reasonable '
                                        'to limit yourself to ten images per collection. Only '
                                        'five random images show in your collection detail view.</br />Show '
                                        'us the fun stuff!')
    caption = models.CharField('Caption',
                               max_length=50,
                               default='',
                               help_text='Provide a short yet descriptive caption describing the '
                                         'image. <br />Be very economical: 50 character limit, but shorter '
                                         'is better. Make adjustments based in image orientation.')
    collection = models.ForeignKey(Collection,
                                   related_name='collections',
                                   verbose_name='Related Collection',
                                   on_delete=models.CASCADE,
                                   default='',
                                   blank=False)

    class Meta:
        verbose_name = 'Collection Image'
        verbose_name_plural = 'Collection Images'
        ordering = ['caption']

    def __str__(self):
        return f"{self.caption}"


class CollectionDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField('Add Document',
                                upload_to='collection/documents/',
                                help_text='Upload documents such as use guides or collection development '
                                          'statements.')
    document_caption = models.CharField('Document Caption',
                                        max_length=255,
                                        default='',
                                        help_text='Provide a short caption describing the document.')
    collection = models.ForeignKey('Collection',
                                   related_name='documents',
                                   verbose_name=u'Related Collection',
                                   on_delete=models.CASCADE,
                                   default='',
                                   blank=True)

    def __str__(self):
        return self.document_caption

    class Meta:
        verbose_name = 'Collection Document'
        verbose_name_plural = 'Collection Documents'
        ordering = ['document_caption']


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

# Extend User model with custom fields
# class AFRUser(models.Model):
#     user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL)
#     institution = models.CharField(blank=True, max_length=100)
#     private_collector = models.BooleanField(default=False)
#     dealer = models.BooleanField(default=False)
