# Generated by Django 3.1.3 on 2020-12-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0008_auto_20201206_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='father_epilepsy',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='mother_epilepsy',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='self_epilepsy',
            field=models.BooleanField(null=True),
        ),
    ]