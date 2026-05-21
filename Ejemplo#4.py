'''Este es un programa para el registro
de notas de un profesor'''
#Imports
import array

#-----------------------------------------------------------------

#Crea las Listas
notas = array.array('f')
nombres = []

#-----------------------------------------------------------------

#Función de crear Menú
def menu():
    print("\tMenú")
    print("1.Ingresar Notas")
    print("2.Mostrar Notas")
    print("3.Salir")

#Agregar la nota
def agregarDatos(listaNotas,listaNombres):
    nombre = input("Ingrese la nombre: ")
    nota = float(input("Ingrese la nota: "))
    listaNotas.append(nota)
    listaNombres.append(nombre)
    return listaNotas, listaNombres

#Imprimir el estudiante y su nota
def mostrarNotas(notas,nombres):
    for i in range(len(notas)):
        print("El estudiante ",nombres[i], " tiene una nota de ",notas[i])
    print()

#-----------------------------------------------------------------

#Flujo principal
while True:
    menu()
    opcion = int(input("Seleccione la opción deseada: "))
    if opcion == 1:
        notas,nombres = agregarDatos(notas,nombres)
    elif opcion == 2:
        mostrarNotas(notas,nombres)
    elif opcion == 3:
        print("Muchas gracias")
        break
    else:
        print("La opción seleccionada no es válida")
