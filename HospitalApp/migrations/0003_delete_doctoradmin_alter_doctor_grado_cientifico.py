# Generated by Django 5.0.1 on 2024-02-04 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0002_doctoradmin_alter_doctor_grado_cientifico'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DoctorAdmin',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='grado_cientifico',
            field=models.CharField(choices=[('Ninguno', 'Ninguno'), ('Doctor', 'Doctor'), ('Máster', 'Máster')], max_length=10, verbose_name='Grado científico'),
        ),
    ]
