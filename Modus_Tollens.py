1# Definición de una función llamada modus_tollens que toma dos argumentos booleanos:
# entregaste_tarea: indica si entregaste la tarea (True o False)
def modus_tollens():
    # Verificamos la primera premisa del Modus Tollens
    entregaste_tarea = int(input("Entregaste la tarea? (1 Si, 0 No): "))
    
    # Verificamos si la entrada es válida (1 o 0)
    while entregaste_tarea != 0 and entregaste_tarea != 1:
        entregaste_tarea = int(input("Valor no válido, ingresa otro (1 Si, 0 No): "))
    
    # Motor de inferencia
    if entregaste_tarea == 1:
        print("Si entregaste la tarea, entonces no tendrás una tarea pendiente.")
        print("Por lo tanto, No tienes tarea pendiente.")
    else:
        print("Si no entregaste la tarea, entonces tendrás una tarea pendiente.")
        print("Por lo tanto, Tienes tarea pendiente.")

# Llamamos a la función modus_tollens
modus_tollens()