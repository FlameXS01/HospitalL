
from django.contrib import admin
from HospitalApp.models import *


class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombrePaciente", "ciPaciente", "direccion","phoneNumber")
    search_fields = ("nombrePaciente","phoneNumber",)
    list_filter = ("nombrePaciente",)




class DoctorAdmin (admin.ModelAdmin):
    list_display = ("nombreDoctor","especialidad","grado_cientifico","ciDoctor")
    search_fields = ("nombreDoctor","especialidad","grado_cientifico")
    list_filter = ("nombreDoctor",)



admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Doctor,DoctorAdmin)
