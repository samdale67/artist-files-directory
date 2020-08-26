# Generated by Django 3.0.5 on 2020-07-10 16:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0044_auto_20200710_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='notes',
            field=ckeditor.fields.RichTextField(blank=True, help_text='Use this field for providing information not accommodated in other fields. This field displays to the public.', max_length=1000, verbose_name='Notes'),
        ),
    ]