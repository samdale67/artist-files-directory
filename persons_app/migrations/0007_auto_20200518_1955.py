# Generated by Django 3.0.5 on 2020-05-18 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons_app', '0006_auto_20200514_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontype',
            name='type_name',
            field=models.CharField(max_length=100, verbose_name='Person Type'),
        ),
    ]