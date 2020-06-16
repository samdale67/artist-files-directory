# Generated by Django 3.0.5 on 2020-06-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collectors_app', '0033_auto_20200605_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collector',
            name='inst_main_name',
            field=models.CharField(blank=True, help_text='If an institutional collection, provide main institution name. If consortium or collaboration, suppy official name or generalized name (use notes field to provide details). If a dealer provide business name.', max_length=255, verbose_name='Institution/Dealer Main Name'),
        ),
    ]
