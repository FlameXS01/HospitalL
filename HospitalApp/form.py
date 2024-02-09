
from django import forms
from HospitalApp.models import*



class Formulario_Paciente (forms.ModelForm):
  class Meta:
     model = Paciente
     fields='__all__'


class Formulario_Doctor (forms.ModelForm):
    especialidad =  forms.ModelChoiceField(queryset= Especialidad.objects.all())

    class Meta :
        model = Doctor
        fields='__all__'

class Formulario_Sala (forms.ModelForm):
    nombre = forms.CharField(required=True)
    piso = forms.CharField(required=True)   
    responsable = forms.ModelChoiceField(queryset= Doctor.objects.all())

    class Meta:
        model = Sala
        fields = '__all__'
   

class Formulario_RegistroPaciente(forms.ModelForm):  
     paciente = forms.ModelChoiceField(queryset= Paciente.objects.all())
     doc = forms.ModelChoiceField(queryset= Doctor.objects.all())
     
     class Meta:
        model = RegistroDPaciente
        fields = '__all__'
    





   