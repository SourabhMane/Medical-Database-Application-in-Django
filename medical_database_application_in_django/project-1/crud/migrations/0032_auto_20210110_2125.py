# Generated by Django 3.1.3 on 2021-01-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0031_auto_20210110_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='chest_pain',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='fainting_spells',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='freq_cold',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='freq_headache',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='hearing_disturb',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='joint_pains',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='short_breath',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='swelling_ankle',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='urinary_disturb',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='vertigo',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='visual_disturb',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='patientoverallmedicaldetails',
            name='weight_loss',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
