# Generated by Django 3.1.3 on 2021-01-17 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0034_auto_20210117_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodurinexray',
            name='albumin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bloodurinexray',
            name='bilirubin_indierct',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bloodurinexray',
            name='chol_hdl_ratio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bloodurinexray',
            name='fbsl',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bloodurinexray',
            name='globumin',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bloodurinexray',
            name='ldl_hdl_ratio',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bloodurinexray',
            name='ppbsl',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bloodurinexray',
            name='total_protein',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='bloodurinexray',
            name='uric_acid',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
