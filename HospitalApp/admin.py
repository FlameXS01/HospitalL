
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


class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    list_filter = ("nombre",)

class RegistroDPacienteAdmin(admin.ModelAdmin):
    list_display = ("paciente", "sala", "enfermedad")
    search_fields = ("paciente", "sala", "enfermedad")
    list_filter = ("paciente", "sala", "enfermedad")


admin.site.register(Paciente,PacienteAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(RegistroDPaciente, RegistroDPacienteAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)

