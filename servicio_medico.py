from cliente.login import Login
from cliente.cambio_pw import Cambio_pw
import sqlite3
from os import system
import time

DATABASE_NAME = "servicios_medicos.db"

isAdmin = -1
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
                    if flag:
                        x, id_c = Cambio_pw(id_cuenta)
                        isAdmin = int(x)
                        print('Vuelve a iniciar sesion')
                    print(id_cuenta)
                    print(isAdmin)
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
            print("1. Revisar productos")
            print("2. Entrar al Foro")
            print("3. Modificar inventario")
            print("4. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    print("Saliendo")
                    return
                elif opcion == 2:
                    print("Saliendo")
                    return
                elif opcion == 3:
                    print("Saliendo")
                    return
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
            print("1. Revisar productos")
            print("2. Carrito")
            print("3. Comprar articulos del carrito")
            print("4. Entrar al Foro")
            print("5. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    print("Saliendo")
                    return
                elif opcion == 2:
                    print("Saliendo")
                    return
                elif opcion == 3:
                    print("Saliendo")
                    return
                elif opcion == 4:
                    print("Saliendo")
                    return
                elif opcion == 5:
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")
main()
