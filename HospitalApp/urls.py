from django.urls import path
from HospitalApp import views

urlpatterns = [
   

    path('paciente/', views.paciente, name="Paciente"),
    path('insertar_paciente/', views.insertar_paciente,name="insertar_paciente"),
    path('editar_paciente/<int:id_paciente>', views.editar_paciente,name="editar_paciente"),
    path('eliminar_paciente/<int:id_paciente>', views.eliminar_paciente,name="eliminar_paciente"),    

]