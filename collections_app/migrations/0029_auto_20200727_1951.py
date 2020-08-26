# Generated by Django 3.0.5 on 2020-07-27 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0010_auto_20200508_1851'),
        ('collections_app', '0028_auto_20200727_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='cities_light.City', verbose_name='Location: City'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='cities_light.Country', verbose_name='Location: Country'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='state_province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collection', to='cities_light.Region', verbose_name='Location: State/Province'),
        ),
    ]