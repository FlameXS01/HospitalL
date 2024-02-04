
from django.contrib import admin
from HospitalApp.models import *


class PacienteAdmin(admin.ModelAdmin):
    list_display = ("nombrePaciente", "ciPaciente", "direccion","phoneNumber")
    search_fields = ("nombrePaciente","phoneNumber",)
    list_filter = ("nombrePaciente",)








admin.site.register(Paciente,PacienteAdmin)
