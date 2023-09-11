# Definición de una función llamada modus_ponens que toma dos argumentos booleanos:
# tarea_pendiente: indica si tienes una tarea pendiente
def modus_ponens():
    # Verificamos la primera premisa del Modus Ponens
    tarea_pendiente = int(input("Tienes una tarea pendiente? (1 Si, 0 No): "))
    
    # Verificamos si la entrada es válida (1 o 0)
    while tarea_pendiente != 0 and tarea_pendiente != 1:
        tarea_pendiente = int(input("Valor no válido, ingresa otro (1 Si, 0 No): "))
    
    # Motor de inferencia
    if tarea_pendiente == 0:
        print("Si no tienes una tarea pendiente, entonces entregaste la tarea.")
        print("Por lo tanto, Entregaste la tarea.")
    else:
        print("Si tienes una tarea pendiente, entonces no entregaste la tarea.")
        print("Por lo tanto, No entregaste la tarea.")

# Llamamos a la función modus_ponens
modus_ponens()