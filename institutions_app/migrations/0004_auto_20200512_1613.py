# Generated by Django 3.0.5 on 2020-05-12 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collections_app', '0009_auto_20200512_0150'),
        ('institutions_app', '0003_auto_20200512_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='inst_collection',
            field=models.ForeignKey(help_text='Create an artist files collection and provide details. Use "General Collection" if describing all files as one combined entry. Create a separate entry for each formally named collection or collection with special characteristics, for example "The Nettie Wheeler Artist Files on Native American Artists." Multiple collections allowed and encouraged.', on_delete=django.db.models.deletion.CASCADE, to='collections_app.Collection'),
        ),
    ]