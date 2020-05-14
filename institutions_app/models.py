from django.db import models


class Institution(models.Model):
    inst_main_name = models.CharField('Main Name',
                                      max_length=255,
                                      help_text='Provide main institution name.',
                                      blank=False)
    inst_sub_name = models.CharField('Secondary Name',
                                     max_length=255,
                                     help_text='Provide name of department, division, etc., responsible for '
                                               'artist files.',
                                     blank=True)
    inst_website = models.URLField('Website',
                                   max_length=255,
                                   help_text='Provide website address related to main institution or '
                                             'department, division, etc., for example, '
                                             '"www.cartermuseum.org/library."',
                                   blank=False)
    inst_email = models.EmailField('Email',
                                   max_length=255,
                                   help_text='Provide best email for answering questions about artist '
                                             'files. Prefer general email such as '
                                             '"library@cartermuseum.org"',
                                   blank=False)
    inst_tel = models.CharField('Telephone',
                                max_length=50,
                                help_text='Provide best telephone contact for answering questions about '
                                          'artist files.',
                                blank=False)
    inst_type = models.ManyToManyField(verbose_name=u'Types',
                                       to='InstitutionType',
                                       related_name='Institution',
                                       blank=False,
                                       default='',
                                       help_text='Choose all types that are relevant. Create a new type if '
                                                 'there is not a fit.')
    inst_collection = models.ForeignKey('collections_app.Collection',
                                        verbose_name=u'Collections',
                                        on_delete=models.CASCADE,
                                        help_text='Create an artist files collection and provide details. '
                                                  'Use "General Collection" if describing all files as one '
                                                  'combined entry. Create a separate entry for each '
                                                  'formally named collection or collection with special '
                                                  'characteristics, for example \"The Nettie Wheeler Artist '
                                                  'Files on Native American Artists.\" Multiple collections '
                                                  'allowed and encouraged.')
    inst_date_created = models.DateField(auto_now_add=True)
    inst_date_saved = models.DateField(auto_now=True)

    def __str__(self):
        return self.inst_main_name + ", " + self.inst_sub_name

    class Meta:
        verbose_name = 'Institution'
        verbose_name_plural = 'Institutions'
        ordering = ['inst_main_name']


class InstitutionType(models.Model):
    type_name = models.CharField('Type',
                                 max_length=100)
    notes = models.TextField(max_length=500, default='', null=True, blank=True)

    def __str__(self):
        return self.type_name

    class Meta:
        verbose_name = 'Institution Type'
        verbose_name_plural = 'Institution Types'
        ordering = ['type_name']
