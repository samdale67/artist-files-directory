# Generated by Django 3.0.5 on 2020-06-01 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0016_collector_other_pref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='other_pref',
            field=models.BooleanField(blank=True, verbose_name='Is other contact a preferred contact?'),
        ),
    ]
