from backend.Clients.login import Login
import sqlite3
from os import system


isAdmin = 0
correo = ""

def main():
    global isAdmin, correo
    conn = sqlite3.connect(host="db", database="sistema_medico", user="postgres", password="postgres")
    cur = conn.cursor()
    conn.commit()
    system("clear")
    while True:
        if isAdmin == 0:
            print("Que desea hacer?")
            print("1. Crear una nueva cuenta")
            print("2. Ingresar a una cuenta existente")
            print("3. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    print("Creando nueva cuenta")
#                    x = Register()
                    #x = Register()
                    print("Registro exitoso")
                    system('clear')
                elif opcion == 2:
                    print("Ingresando a una cuenta existente")
                    x, y = Login()
                    correo = y
                    isAdmin = int(x)
                    system('clear')
                elif opcion == 3:
                    print("Saliendo")
                    system('clear')
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")
        '''
        elif isAdmin == 1:
            print('Soy Admin')
            print("Que desea hacer?")
            print("1. Revisar productos")
            print("2. Entrar al Foro")
            print("3. Modificar inventario")
            print("4. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    catalogo()
                elif opcion == 2:
                    preguntas_foro(isAdmin,correo)
                    system('clear')
                elif opcion == 3:
                    inventario_cli()
                    system('clear')
                elif opcion == 4:
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")
        elif isAdmin == 2:
            print('Soy Cliente')
            print("Que desea hacer?")
            print("1. Revisar productos")
            print("2. Carrito")
            print("3. Comprar articulos del carrito")
            print("4. Entrar al Foro")
            print("5. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    catalogo()
                elif opcion == 2:
                    carro_productos = general(carro_productos)
                    system('clear')
                elif opcion == 3:
                    carro_productos = compras(carro_productos, correo)
                elif opcion == 4:
                    preguntas_foro(isAdmin,correo)
                    system('clear')
                elif opcion == 5:
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")
        elif isAdmin == 3:
            print("Soy Soporte")
            print("1. Entrar al Foro")
            print("2. Salir")
            try:
                opcion = int(input("Ingrese una opcion: ").strip())
                if opcion == 1:
                    preguntas_foro(isAdmin,correo)
                    system('clear')
                elif opcion == 2:
                    print("Saliendo")
                    return
                else:
                    print("Opcion invalida")
            except:
                print("Opcion invalida")
        '''
main()