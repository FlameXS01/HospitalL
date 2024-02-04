
from django import forms
from HospitalApp.models import*



class Formulario_Paciente (forms.Form):
    nombrePaciente = forms.CharField(required=True)
    ciPaciente = forms.CharField(required=True)
    especialidad = forms.CharField(required=True)
    gradoCientifico = forms.CharField(required=True)









   