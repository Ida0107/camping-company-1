# Generated by Django 2.0.7 on 2018-09-17 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0002_vehiclecheck_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiclecheck',
            name='customer',
        ),
        migrations.AddField(
            model_name='vehiclecheck',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_check', to=settings.AUTH_USER_MODEL),
        ),
    ]
