"""
Escribir un programa en Python que administre una lista de tareas. El programa debe permitir al 
usuario agregar, eliminar y listar tareas. Cada tarea tendrá un nombre, una descripción y una
prioridad (alta, media, baja). Además, habrá diferentes tipos de tareas: TablaGeneral y 
TablasConFecha, cada una con característias adicionales.

Requisitos del Código:

1. El programa debe permitir agregar una nueva tarea.
2. El programa debe permitir eliminar una tarea existente.
3. El programa debe permitir listar todas las tareas con sus detalles.
4. El programa debe estar diseñado utilizando POO e incluir herencia.
"""
lista = []
class TablaGeneral:
    def __init__(self, nombre, descripcion, prioridad):
        self.nombre = nombre
        self.descripcion = descripcion
        self.prioridad = prioridad
    
    def mostrarlista(self):
        for indice,tarea in enumerate(lista):
            print(f'{indice}: {tarea}')

    def agregar(self):
        while True:
            agregar_producto = str(input('Ingrese el nombre del producto: '))
            lista.append(agregar_producto)
            break

    def eliminar(self):
            print('¿Qué producto desea eliminar?')
            TablaGeneral.mostrarlista()
            while True: 
                eliminar_producto = int(input('Ingrese una opción:'))
                if eliminar_producto in lista:
                    lista.pop(eliminar_producto)
                else:
                    print('Por favor, ingrese una opción válida.')
                    break
    def listartarea(self):
        print(f'Tarea: {self.nombre}\nDescripción: {self.descripcion}\nPrioridad: {self.prioridad}')

class TablaConFecha(TablaGeneral):
    def __init__(self, nombre, descripcion, prioridad, fecha):
        super().__init__(nombre, descripcion, prioridad)
        self.fecha = fecha
    super().mostrarlista()
    super().agregar()
    super().eliminar()
    super().listartarea()
    def listarfecha(self):
        print(f'Fecha: {self.fecha}')

def sistema():
    print('Bienvenido al sistema.\Ingrese [1] para continuar\nIngrese[2] para salir.')
    while True:
        sistema = int(input('Ingrese una opción: '))
        if sistema == 1:
            print('Bienvenido. ¿Qué desea hacer?')
            print('[1]  Agregar tarea\n[2] Eliminar tarea\n[3] Mostrar tareas')
            opcionUsuario =  int(input('Ingrese una opción: '))
            if opcionUsuario == 1:
                while True:
                    print('¿Desea agregar fecha?\n[1] Sí. [2] No.')
                    opcionAgregar = int(input('Ingrese una opción: '))
                    if opcionAgregar == 1:
                        TablaGeneral.agregar()
                        continue
                    elif opcionAgregar == 2:
                        TablaConFecha.agregar()
                        continue
                    else:
                        print('Por favor, ingrese una opción válida.')
                        break
            elif opcionUsuario == 2:
                TablaGeneral.eliminar()
            elif opcionUsuario == 3:
                TablaGeneral.listartarea()
                if lista == []:
                    print('No hay tareas')
            else:
                print('Opción no válida')
        if sistema == 2:
            break

sistema()