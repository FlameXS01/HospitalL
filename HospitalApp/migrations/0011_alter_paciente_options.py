# Generated by Django 5.0.1 on 2024-02-08 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0010_alter_paciente_options_alter_doctor_grado_cientifico'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='paciente',
            options={'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
    ]
