# Generated by Django 3.1.3 on 2021-01-10 13:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0020_auto_20201225_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientoverallmedicaldetails',
            name='addictions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, null=True, size=None),
        ),
    ]
