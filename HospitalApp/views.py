
from HospitalApp.models import*
from HospitalApp.form import*
from django.shortcuts import render,redirect,get_object_or_404


# ===========================================Paciente====================================================

def paciente(request):
    paciente = Paciente.objects.all()
    
    return render(request,'paciente/Paciente.html',{"pacientes1":paciente})


def insertar_clase(request):
    
    miformulario = Formulario_Paciente()
    pacienteFormularios = Paciente.objects.all()
    
    if request.method == "POST":
        miformulario = Formulario_Paciente(data = request.POST)
        if miformulario.is_valid():
            
            paciente = Paciente()
            
            paciente.nombrePaciente = miformulario.cleaned_data["nombrePaciente"]
            paciente.ciPaciente = miformulario.cleaned_data["ciPaciente"]
            paciente.direccion = miformulario.cleaned_data["direccion"]
            paciente.phoneNumber = miformulario.cleaned_data["phoneNumber"]

            paciente.save()

            return redirect("Paciente")
    
    return render(request,'paciente/insertar.html',{"claseFormularios":pacienteFormularios,"miformulario":miformulario})
def insertar_paciente(request):
    
    form=Formulario_Paciente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Paciente')
    else: print('Error')
    return render(request, 'paciente/insertar.html',{'miformulario':form})
    
def editar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    formulario = Formulario_Paciente(instance=paciente)
    if request.method == 'POST':
        formulario = Formulario_Paciente(request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            return redirect('Paciente')
    return render(request, 'paciente/editar.html', {'miformulario': formulario})

def eliminar_paciente(request,id_clase):
    
    paciente= Paciente.objects.get(pk = id_clase)
    
    paciente.delete()
    
    return redirect("Paciente")

