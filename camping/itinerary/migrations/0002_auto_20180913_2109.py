# Generated by Django 2.0.7 on 2018-09-13 15:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerary',
            old_name='created',
            new_name='created_time',
        ),
        migrations.AddField(
            model_name='itinerary',
            name='created_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]