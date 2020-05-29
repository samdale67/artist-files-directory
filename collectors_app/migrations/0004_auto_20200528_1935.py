# Generated by Django 3.0.5 on 2020-05-28 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0003_auto_20200528_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='person_first_name',
            field=models.CharField(help_text='If a personal collection, provide first name of collector. If institution, provide first name of person filling out this form.', max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='collector',
            name='person_last_name',
            field=models.CharField(help_text='If a personal collection, provide last name of collector. If institution, provide last name of person filling out this form.', max_length=255, verbose_name='Last Name'),
        ),
    ]