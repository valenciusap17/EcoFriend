# Generated by Django 4.1 on 2022-10-27 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_alter_footprint_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footprint',
            name='date',
            field=models.DateField(default='27.10.2022 10:02:46'),
        ),
    ]
