from cliente.login import Login
from cliente.cambio_pw import Cambio_pw
from cliente.agregar_paciente import agregar_paciente
from cliente.delete_paciente import delete_paciente
from cliente.edit_paciente import edit_paciente
from cliente.agregar_diagnostico import Agregar_diagnostico
from cliente.historial_medico import historial_medico
from cliente.agregar_cuenta import agregar_medico
from cliente.delete_medico import delete_medico

import sqlite3
from os import system
import time

DATABASE_NAME = "servicios/servicios_medicos.db"

isAdmin = -1
id_cuenta = ""

def main():
    global isAdmin, id_cuenta
    conn = sqlite3.connect(DATABASE_NAME)
    cur = conn.cursor()
    conn.commit()
    system("clear")
    while True:

        if isAdmin < 0:
            print("Que desea hacer?")
            print("1. Ingresar a una cuenta existente")
            print("2. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    print("Ingresando a una cuenta existente")
                    id_cuenta, flag = Login()
                    #verificar que sea admin con id_cuenta == '0'
                    if id_cuenta == '0':
                        isAdmin = 0
                    else:
                        if not int(flag):
                            x, id_cuenta = Cambio_pw(id_cuenta)
                            if int(x) == -2:
                                print('Correo o contraseña incorrecta')
                            else:
                                isAdmin = int(x)
                                print('Su contraseña se cambio exitosamente')
                        else:
                            isAdmin = int(flag)
#                    system('clear')
                elif opcion == 2:
                    print("Saliendo")
                    system('clear')
                    return
                else:
                    print("Opcion invalida A")
            except:
                print("Error ingreso de sesion, verificar datos")
        
        elif isAdmin == 0:
            print('Soy Admin')
            print("Que desea hacer?")
            print("1. Añadir cuenta")
            print("2. Eliminar paciente")
            print("3. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    var = agregar_medico()
                    if var == '1':
                        print("Cuenta creada correctamente")
                    else:
                        print("Error en crear cuenta")
                elif opcion == 2:
                    delete = delete_paciente()
                    if int(delete) == -1:
                        print("Se han borrado los datos asociados al paciente de manera satisfactoria")
                    else:
                        print("No se han encontrado datos asociados al paciente")
                elif opcion == 3:
                    print("Saliendo")
                    return     
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")
        else:
            print('Soy Medico')
            print("Que desea hacer?")
            print("1. añadir paciente")
            print("2. añadir diagnostico")
            print("3. editar paciente")
            print("4. Consultar Historial Medico de un paciente")
            print("5. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    agregar_paciente()
                elif opcion == 2:
                    diagno = Agregar_diagnostico("19689912-k")
                    if int(diagno) == 1:
                        print("Se ha agregado el diagnostico")
                    else:
                        print("No se ha agregado el diagnostico")
                    print("Saliendo")
                elif opcion == 3:
                    print("Editar Paciente")
                    edit_paciente()

                elif opcion == 4:
                    historial_medico()
                    print("Saliendo")
                elif opcion == 5:
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida A")
            except Exception as e:
                print(e)
                print("Opcion invalida B")
main()