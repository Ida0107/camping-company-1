# Generated by Django 2.0.7 on 2018-09-17 05:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('equipment', '0002_equipmentcheck_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipmentcheck',
            name='customer',
        ),
        migrations.AddField(
            model_name='equipmentcheck',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='equipment_check', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]