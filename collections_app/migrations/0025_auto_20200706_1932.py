# Generated by Django 3.0.5 on 2020-07-06 19:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0024_auto_20200706_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Use this field for information that does not fit elsewhere.', max_length=1000, verbose_name='Notes'),
        ),
    ]
