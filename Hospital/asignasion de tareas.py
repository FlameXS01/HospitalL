#import numpy as np
import itertools

def asignar_tareas(tiempo_tareas):
    trabajadores = tiempo_tareas.keys()
    tareas = list(tiempo_tareas[trabajadores[0]].keys())
    
    min_tiempo = float('inf')
    mejor_asignacion = None
    
    alltask = itertools.permutations(tareas)
    for permutacion in  alltask:
        tiempo_total = sum(tiempo_tareas[trabajador][tarea] for trabajador, tarea in zip(trabajadores, permutacion))
        if tiempo_total < min_tiempo:
            min_tiempo = tiempo_total
            mejor_asignacion = dict(zip(trabajadores, permutacion))
    
    return mejor_asignacion, min_tiempo

# Ejemplo de uso
tiempo_tareas = {
    'Jhon': {'A': 1, 'B': 4, 'C': 6},
    'Karen': {'A': 9, 'B': 7, 'C': 10},
    'Thomas': {'A': 4, 'B': 5, 'C': 11}
}

mejor_asignacion, min_tiempo = asignar_tareas(tiempo_tareas)
print(f"La mejor asignación es: {mejor_asignacion} con un tiempo total de: {min_tiempo}")
