# Generated by Django 3.0.5 on 2020-06-05 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0031_collector_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='inst_main_name',
            field=models.CharField(blank=True, help_text='If an institutional collection, provide main institution name. If a dealer, provide business name. If consortium or collaboration, suppy official name or summarized name of consortium or collaboration.', max_length=255, verbose_name='Institution/Dealer Main Name'),
        ),
    ]
