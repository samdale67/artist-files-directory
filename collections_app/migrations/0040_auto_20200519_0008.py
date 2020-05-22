# Generated by Django 3.0.5 on 2020-05-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0039_auto_20200519_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionsubjectname',
            name='coll_sub_name',
            field=models.CharField(help_text='Use preferred <a href="http://www.viaf.org" target="_blank">VIAF</a> form of name. Remove delimiters and subfields, e.g. "Hughston, Milan R., 1954- "', max_length=100, verbose_name='Subject: Name'),
        ),
    ]
