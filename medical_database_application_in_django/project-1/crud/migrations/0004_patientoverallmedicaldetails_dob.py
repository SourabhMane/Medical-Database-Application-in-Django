# Generated by Django 3.1.3 on 2020-11-25 17:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_patientoverallmedicaldetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='%m/%d/%Y'),
            preserve_default=False,
        ),
    ]
