# Generated by Django 3.0.5 on 2020-06-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0029_auto_20200605_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='person_first_name',
            field=models.CharField(blank=True, help_text='Only use for first name of private collector.', max_length=255, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='collector',
            name='person_last_name',
            field=models.CharField(blank=True, help_text='Only use for last name of private collector.', max_length=255, verbose_name='Last Name'),
        ),
    ]
