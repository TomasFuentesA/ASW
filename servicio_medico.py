from cliente.login import Login
from cliente.cambio_pw import Cambio_pw
from cliente.agregar_paciente import agregar_paciente
from cliente.delete_paciente import delete_paciente
from cliente.edit_paciente import edit_paciente
from cliente.agregar_diagnostico import Agregar_diagnostico
from cliente.historial_medico import historial_medico
from cliente.agregar_cuenta import agregar_medico

import sqlite3
from os import system
import time

DATABASE_NAME = "servicios/servicios_medicos.db"

isAdmin = 10
correo = ""

def main():
    global isAdmin, correo
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
                    isAdmin = int(id_cuenta)
                    print(flag)
                    time.sleep(10)
                    if not int(flag):
                        x, id_c = Cambio_pw(id_cuenta)
                        isAdmin = int(x)
                        print('Vuelve a iniciar sesion')
                    print(id_cuenta)
                    system('clear')
                elif opcion == 2:
                    print("Saliendo")
                    system('clear')
                    return
                else:
                    print("Opcion invalida A")
            except:
                print("Opcion invalida B")
        
        elif isAdmin == 0:
            print('Soy Admin')
            print("Que desea hacer?")
            print("1. Añadir cuenta")
            print("2. Entrar al Foro")
            print("3. Eliminar paciente")
            print("4. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    agregar_medico()
                elif opcion == 2:
                    print("Saliendo")
                    return
                elif opcion == 3:
                    delete = delete_paciente()
                    if int(delete) == -1:
                        print("Se ha borrado el paciente de manera satisfactoria")
                        time.sleep(2)
                    system('clear')  
                elif opcion == 4:
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
                    print("agregado")
                    time.sleep(5)

                elif opcion == 2:
                    Agregar_diagnostico(isAdmin)
                    print("Saliendo")

                elif opcion == 3:
                    print("Editar Paciente")
                    editar = edit_paciente()
                    if int(editar) == 1:
                        print("Se ha modificado el paciente de manera satisfactoria")
                        time.sleep(2)
                    else:
                        print("Error al ingresar paciente o datos a cambiar")
                        time.sleep(2)
                    system('clear')  

                elif opcion == 4:
                    historial_medico()

                elif opcion == 5:
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")
main()