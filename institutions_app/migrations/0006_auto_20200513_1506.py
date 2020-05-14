# Generated by Django 3.0.5 on 2020-05-13 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institutions_app', '0005_auto_20200513_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='inst_sub_name',
            field=models.CharField(blank=True, help_text='Provide name of department, division, etc., responsible for artist files.', max_length=255, verbose_name='Secondary Name'),
        ),
    ]