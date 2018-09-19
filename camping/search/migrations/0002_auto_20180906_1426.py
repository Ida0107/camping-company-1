# Generated by Django 2.0.7 on 2018-09-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='city',
            field=models.TextField(default='delhi', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='search',
            name='totalDays',
            field=models.PositiveIntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='search',
            name='tripDay',
            field=models.DateField(blank=True, null=True),
        ),
    ]