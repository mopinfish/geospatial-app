# Generated by Django 3.0.7 on 2020-06-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_border_busstop_facility_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='border',
            name='n03_003',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
