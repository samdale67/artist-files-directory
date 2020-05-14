# Generated by Django 3.0.5 on 2020-05-13 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0017_auto_20200513_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionspecialformat',
            name='coll_special_format',
            field=models.CharField(max_length=100, verbose_name='Special Format'),
        ),
        migrations.AlterField(
            model_name='collectionspecialformat',
            name='coll_special_format_thesaurus',
            field=models.CharField(choices=[('TGM', 'Thesaurus for Graphic Materials'), ('LCGFT', 'LC Genre/Form Terms'), ('Wikipedia', 'Wikipedia'), ('Other', 'Other')], max_length=10, verbose_name='Thesaurus'),
        ),
        migrations.AlterField(
            model_name='collectionspecialformat',
            name='coll_special_format_url',
            field=models.URLField(help_text='Provide permalink from id.loc.gov or Wikipedia URL.', max_length=255, verbose_name='Thesaurus Website'),
        ),
    ]