# Generated by Django 3.0.5 on 2020-07-06 19:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0041_auto_20200701_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, max_length=1000, verbose_name='Notes'),
        ),
    ]
