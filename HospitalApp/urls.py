from django.urls import path
from HospitalApp import views

urlpatterns = [
   
       path('', views.base, name="base"),


    path('paciente/', views.paciente, name="Paciente"),
    path('insertar_paciente/', views.insertar_paciente,name="insertar_paciente"),
    path('editar_paciente/<int:id_paciente>', views.editar_paciente,name="editar_paciente"),
    path('eliminar_paciente/<int:id_paciente>', views.eliminar_paciente,name="eliminar_paciente"),    


    path('doctor/', views.doctor, name="Doctor"),
    path('insertar_doctor/', views.insertar_doctor,name="insertar_doctor"),
    path('editar_doctor/<int:id_doctor>', views.editar_doctor,name="editar_doctor"),
    path('eliminar_doctor/<int:id_doctor>', views.eliminar_doctor,name="eliminar_doctor"), 

    path('sala/', views.sala, name="Sala"),
    path('insertar_sala/', views.insertar_sala,name="insertar_sala"),
    path('editar_sala/<int:idSala>', views.editar_sala,name="editar_sala"),
    path('eliminar_sala/<int:idSala>', views.eliminar_sala,name="eliminar_sala"), 



    path('registroPaciente/', views.registroPaciente, name="RegistroPaciente"),
    path('insertar_registro/', views.insertar_registro,name="insertar_registro"),
    path('editar_registro/<int:idRegistroPaciente>', views.editar_registro,name="editar_registro"),
    path('eliminar_registro/<int:idRegistroPaciente>', views.eliminar_registro,name="eliminar_registro"), 

]