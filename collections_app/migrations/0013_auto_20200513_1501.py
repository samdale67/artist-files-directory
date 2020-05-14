# Generated by Django 3.0.5 on 2020-05-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0012_auto_20200513_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_city',
            field=models.CharField(help_text='Important for providing access to collections located in specific cities.', max_length=255, verbose_name='Location - City'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_country',
            field=models.CharField(help_text='Important for providing access to collections located in specific countries.', max_length=255, verbose_name='Location - Country'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='coll_loc_state_prov',
            field=models.CharField(help_text='Important for providing access to collections located in specific states or provinces.', max_length=255, verbose_name='Location - State/Province'),
        ),
    ]