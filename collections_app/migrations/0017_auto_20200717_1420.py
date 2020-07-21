# Generated by Django 3.0.5 on 2020-07-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0016_auto_20200716_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionimage',
            name='caption',
            field=models.CharField(default='', help_text='Provide a short yet descriptive caption describing the image. <br />Be very economical: 35 character limit, but shorter is better.', max_length=50, verbose_name='Caption'),
        ),
    ]
