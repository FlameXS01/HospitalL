from django.db import models

grado_cientifico = {
    ('Ninguno','Ninguno'),
    ('Máster','Máster'),
    ('Doctor','Doctor'),
}

# Create your models here.
class Paciente (models.Model):
    id_paciente = models.BigAutoField(primary_key=True)
    nombrePaciente = models.CharField(max_length=50,verbose_name='Nombre')
    ciPaciente = models.CharField(max_length=50,verbose_name='CI')
    direccion =  models.CharField(max_length=200,verbose_name='Direccion')
    phoneNumber = models.IntegerField(max_length=10, verbose_name='Numeo de telefono')
    
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        

    def __str__(self):
        return self.nombrePaciente

class Doctor (models.Model):
    id_doctor = models.BigAutoField(primary_key=True)
    nombreDoctor = models.CharField(max_length=50,verbose_name='Nombre')
    especialidad = models.CharField(max_length=50,verbose_name='Escpecialidad')
    grado_cientifico = models.CharField(max_length=10,verbose_name='Grado científico',choices=grado_cientifico)
    ciDoctor = models.CharField(max_length=50,verbose_name='CI')
    def __str__(self) :
        return self.nombreDoctor



class Sala (models.Model):
    idSala = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    piso = models.IntegerField(verbose_name='Piso')
    responsable = models.ForeignKey(Doctor,blank=True, null=True,on_delete=models.CASCADE)

    def __str__(self) :
        return self.nombre

class RegistroDPaciente (models.Model):
    idRegistroPaciente = models.BigAutoField(primary_key=True)
    paciente  = models.OneToOneField(Paciente,blank=True, null=True,on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala,blank=True, null=True,on_delete=models.CASCADE)
    enfermedad =  models.CharField(max_length=50,verbose_name='Enfermedad')
    doc = models.ForeignKey(Doctor,blank=True, null=True,on_delete=models.DO_NOTHING)

class Especialidad (models.Model):
    idEspecial = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre de la especialidad')

    def __str__(self) :
        return self.nombre
