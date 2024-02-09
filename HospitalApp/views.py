
from HospitalApp.models import*
from HospitalApp.form import*
from django.shortcuts import render,redirect,get_object_or_404


def base (request):
    return render(request,'base/base.html')


# ===========================================Paciente====================================================



def paciente(request):
    paciente = Paciente.objects.all()
    
    return render(request,'paciente/Paciente.html',{"pacientes1":paciente})


def insertar_paciente(request):
    
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
    
    return render(request,'paciente/insertar_paciente.html',{"claseFormularios":pacienteFormularios,"miformulario":miformulario})
def insertar_paciente(request):
    
    form=Formulario_Paciente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Paciente')
    else: print('Error')
    return render(request, 'paciente/insertar_paciente.html',{'miformulario':form})
    
def editar_paciente(request, id_paciente):
    paciente = Paciente.objects.get(id_paciente=id_paciente)
    formulario = Formulario_Paciente(instance=paciente)
    if request.method == 'POST':
        formulario = Formulario_Paciente(request.POST, instance=paciente)
        if formulario.is_valid():
            formulario.save()
            return redirect('Paciente')
    return render(request, 'paciente/editar_paciente.html', {'miformulario': formulario})

def eliminar_paciente(request,id_paciente):
    
    paciente= Paciente.objects.get(pk = id_paciente)
    
    paciente.delete()
    
    return redirect("Paciente")





# ======================================Doctor====================================================

def doctor(request):
    doctor = Doctor.objects.all()
    
    return render(request,'doctor/Doctor.html',{"doctors1":doctor})


def insertar_doctor(request):
    
    miformulario = Formulario_Doctor()
    doctorFormularios = Doctor.objects.all()
    
    if request.method == "POST":
        miformulario = Formulario_Doctor(data = request.POST)
        if miformulario.is_valid():
            
            doctor = Doctor()

            doctor.nombreDoctor = miformulario.cleaned_data["nombreDoctor"]
            doctor.ciDoctor = miformulario.cleaned_data["ciDoctor"]
            doctor.especialidad = miformulario.cleaned_data["especialidad"]
            doctor.grado_cientifico = miformulario.cleaned_data["grado cientifico"]

            doctor.save()

            return redirect("Doctor")
    
    return render(request,'doctor/insertar_doctor.html',{"claseFormularios":doctorFormularios,"miformulario":miformulario})
def insertar_doctor(request):
    
    form=Formulario_Doctor(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Doctor')
    else: print('Error')
    return render(request, 'doctor/insertar_doctor.html',{'miformulario':form})
    
def editar_doctor(request, id_doctor):
    doctor = Doctor.objects.get(id_doctor=id_doctor)
    formulario = Formulario_Doctor(instance=doctor)
    if request.method == 'POST':
        formulario = Formulario_Doctor(request.POST, instance=doctor)
        if formulario.is_valid():
            formulario.save()
            return redirect('Doctor')
    return render(request, 'doctor/editar_doctor.html', {'miformulario': formulario})

def eliminar_doctor(request,id_doctor):
    
    doctor= Doctor.objects.get(pk = id_doctor)
    
    doctor.delete()
    
    return redirect("Doctor")




# ======================================Sala====================================================

def sala(request):
    sala = Sala.objects.all()
    
    return render(request,'sala/Sala.html',{"salas1":sala})


def insertar_sala(request):
    
    miformulario = Formulario_Sala()
    salaFormularios = Sala.objects.all()
    
    if request.method == "POST":
        miformulario = Formulario_Sala(data = request.POST)
        if miformulario.is_valid():
            
            sala = Sala()

            sala.nombre = miformulario.cleaned_data["nombre"]
            sala.piso = miformulario.cleaned_data["piso"]
            sala.responsable = miformulario.cleaned_data["responsable"]

            sala.save()

            return redirect("Sala")
    
    return render(request,'sala/insertar_sala.html',{"claseFormularios":salaFormularios,"miformulario":miformulario})
def insertar_sala(request):
    
    form=Formulario_Sala(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('Sala')
    else: print('Error')
    return render(request, 'sala/insertar_sala.html',{'miformulario':form})
    
def editar_sala(request, idSala):
    sala = Sala.objects.get(idSala=idSala)
    formulario = Formulario_Sala(instance=sala)
    if request.method == 'POST':
        formulario = Formulario_Sala(request.POST, instance=sala)
        if formulario.is_valid():
            formulario.save()
            return redirect('Sala')
    return render(request, 'sala/editar_sala.html', {'miformulario': formulario})

def eliminar_sala(request,idSala):
    
    sala= Sala.objects.get(pk = idSala)
    
    sala.delete()
    
    return redirect("Sala")



# ======================================Registro de pacientes====================================================

def registroPaciente(request):
    registroPaciente = RegistroDPaciente.objects.all()
    
    return render(request,'registroPaciente/registroPaciente.html',{"registros":registroPaciente})


def insertar_registro(request):
    
    miformulario = Formulario_RegistroPaciente()
    registroFormularios = RegistroDPaciente.objects.all()
    
    if request.method == "POST":
        miformulario = Formulario_RegistroPaciente(data = request.POST)
        if miformulario.is_valid():
            
            registroDPaciente = RegistroDPaciente()

            registroDPaciente.paciente = miformulario.cleaned_data["paciente"]
            registroDPaciente.doc = miformulario.cleaned_data["doc"]
            registroDPaciente.enfermedad = miformulario.cleaned_data["enfermedad"]
            registroDPaciente.sala = miformulario.cleaned_data["sala"]


            registroDPaciente.save()

            return redirect("RegistroPaciente")
    
    return render(request,'registroPaciente/insertar_registro.html',{"claseFormularios":registroFormularios,"miformulario":miformulario})
def insertar_registro(request):
    
    form=Formulario_RegistroPaciente(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('RegistroPaciente')
    else: print('Error')
    return render(request, 'registroPaciente/insertar_registro.html',{'miformulario':form})
    
def editar_registro(request, idRegistroPaciente):
    registroPaciente = RegistroDPaciente.objects.get(idRegistroPaciente=idRegistroPaciente)
    formulario = Formulario_RegistroPaciente(instance=registroPaciente)
    if request.method == 'POST':
        formulario = Formulario_Sala(request.POST, instance=registroPaciente)
        if formulario.is_valid():
            formulario.save()
            return redirect('RegistroPaciente')
    return render(request, 'registroPaciente/editar_registro.html', {'miformulario': formulario})

def eliminar_registro(request,idRegistroPaciente):
    
    registroPaciente= RegistroDPaciente.objects.get(pk = idRegistroPaciente)
    
    registroPaciente.delete()
    
    return redirect("RegistroPaciente")