# Generated by Django 3.0.7 on 2020-06-16 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0004_auto_20200616_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busstop',
            name='p11_004_19',
            field=models.CharField(max_length=256, null=True),
        ),
    ]