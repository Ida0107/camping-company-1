# Generated by Django 2.0.7 on 2018-09-07 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20180906_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='city',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='search',
            name='totalDays',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
