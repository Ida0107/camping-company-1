# Generated by Django 2.0.7 on 2018-09-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0005_auto_20180913_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='destination',
            field=models.ManyToManyField(blank=True, related_name='trips', to='destination.Destination'),
        ),
    ]
