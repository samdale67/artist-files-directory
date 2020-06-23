# Generated by Django 3.0.5 on 2020-06-18 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectionimage',
            name='image_caption',
        ),
        migrations.AddField(
            model_name='collectionimage',
            name='caption',
            field=models.CharField(default='', max_length=255, verbose_name='Image Caption'),
        ),
    ]