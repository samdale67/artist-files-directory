# Generated by Django 3.0.5 on 2020-05-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0002_auto_20200527_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='email',
            field=models.EmailField(help_text='Provide best email for answering questions about artist files. If an institution, prefer general email such as "library@cartermuseum.org"', max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='collector',
            name='person_first_name',
            field=models.CharField(help_text='If a personal collection, provide first name of collector. If institution, first name of main contact for answering questions about artist files collections.', max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='collector',
            name='person_last_name',
            field=models.CharField(help_text='If a personal collection, provide last name of collector. If institution, last name of main contact for answering questions about artist files collections.', max_length=255, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='collector',
            name='telephone',
            field=models.CharField(blank=True, help_text='Provide best telephone contact for answering questions about artist files.', max_length=50, verbose_name='Telephone'),
        ),
    ]
