# Generated by Django 3.1.3 on 2020-12-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0011_auto_20201208_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodurinexray',
            name='patient_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='form7details',
            name='patient_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='stoolreport',
            name='patient_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]