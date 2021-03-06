# Generated by Django 3.1.3 on 2020-11-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_member_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientOverallMedicalDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40)),
                ('organization', models.CharField(max_length=40)),
                ('address', models.CharField(blank=True, max_length=10)),
                ('department', models.TextField(max_length=255)),
                ('id_mark', models.TextField(max_length=255)),
                ('gender', models.CharField(blank=True, max_length=10)),
                ('married_stat', models.CharField(blank=True, max_length=10)),
                ('desig', models.CharField(blank=True, max_length=10)),
                ('age', models.CharField(blank=True, max_length=10)),
                ('date', models.DateField(verbose_name='%m/%d/%Y')),
                ('present_complains', models.TextField(max_length=255)),
                ('self_hypertension', models.CharField(blank=True, max_length=10)),
                ('self_diabetes', models.CharField(blank=True, max_length=10)),
                ('self_heartdisease', models.CharField(blank=True, max_length=10)),
                ('self_tuberculosis', models.CharField(blank=True, max_length=10)),
                ('self_cancer', models.CharField(blank=True, max_length=10)),
                ('self_asthama', models.CharField(blank=True, max_length=10)),
                ('self_stroke', models.CharField(blank=True, max_length=10)),
                ('father_hypertension', models.CharField(blank=True, max_length=10)),
                ('father_diabetes', models.CharField(blank=True, max_length=10)),
                ('father_heartdisease', models.CharField(blank=True, max_length=10)),
                ('father_tuberculosis', models.CharField(blank=True, max_length=10)),
                ('father_cancer', models.CharField(blank=True, max_length=10)),
                ('father_asthama', models.CharField(blank=True, max_length=10)),
                ('father_stroke', models.CharField(blank=True, max_length=10)),
                ('mother_hypertension', models.CharField(blank=True, max_length=10)),
                ('mother_diabetes', models.CharField(blank=True, max_length=10)),
                ('mother_heartdisease', models.CharField(blank=True, max_length=10)),
                ('mother_tuberculosis', models.CharField(blank=True, max_length=10)),
                ('mother_cancer', models.CharField(blank=True, max_length=10)),
                ('mother_asthama', models.CharField(blank=True, max_length=10)),
                ('mother_stroke', models.CharField(blank=True, max_length=10)),
            ],
        ),
    ]
