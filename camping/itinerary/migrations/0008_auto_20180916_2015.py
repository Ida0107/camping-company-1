# Generated by Django 2.0.7 on 2018-09-16 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0007_itinerary_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
