# Generated by Django 3.1.3 on 2020-12-13 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0016_auto_20201213_1630'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stoolreport',
            name='age',
        ),
        migrations.RemoveField(
            model_name='stoolreport',
            name='gender',
        ),
    ]