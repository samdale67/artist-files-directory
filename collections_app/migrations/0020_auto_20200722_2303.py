# Generated by Django 3.0.5 on 2020-07-22 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0019_auto_20200717_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionimage',
            name='caption',
            field=models.CharField(default='', help_text='Provide a short yet descriptive caption describing the image. <br />Be very economical: 50 character limit, but shorter is better. The directory favors images with horizontal orientation.', max_length=50, verbose_name='Caption'),
        ),
    ]