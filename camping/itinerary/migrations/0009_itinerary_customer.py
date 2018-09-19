# Generated by Django 2.0.7 on 2018-09-16 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('itinerary', '0008_auto_20180916_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='custs', to='customer.Customer'),
        ),
    ]