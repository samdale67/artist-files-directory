# Generated by Django 3.0.5 on 2020-06-30 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0039_auto_20200623_1835'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collector',
            options={'ordering': ['sort_name'], 'verbose_name': 'Collector', 'verbose_name_plural': '** Collectors'},
        ),
    ]