# Generated by Django 3.0.5 on 2020-05-14 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('institutions_app', '0011_auto_20200514_0024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ['inst_main_name'], 'verbose_name': 'Institution', 'verbose_name_plural': 'Institutions'},
        ),
        migrations.AlterModelOptions(
            name='institutiontype',
            options={'ordering': ['type_name'], 'verbose_name': 'Institution Type', 'verbose_name_plural': 'Institution Types'},
        ),
    ]
