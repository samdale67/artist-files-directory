# Generated by Django 3.0.5 on 2020-07-01 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0018_auto_20200701_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionimage',
            name='collection',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='collections_app.Collection', verbose_name='Related Collection'),
        ),
    ]
