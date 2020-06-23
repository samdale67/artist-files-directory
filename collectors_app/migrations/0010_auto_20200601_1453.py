# Generated by Django 3.0.5 on 2020-06-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0009_auto_20200601_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='telephone_pref',
            field=models.BooleanField(blank=True, help_text='Is a telephone call the preferred method of contact?', verbose_name='Preferred Contact'),
        ),
    ]