import socket, pickle
import sys, json


def edit_paciente(): #pasar parametro usuario
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    id_paciente = input("Ingrese RUT paciente: ")
    print("Ingrese el dato en el campo que corresponde")
    print("Si no desea editar alguno, presione enter para revisar el siguiente.")
    nombre_s = input("Ingrese cambio nombre: ")
    apellido_s = input("Ingrese cambio apellido: ")
    edad= input("Ingrese cambio edad: ")
    sexo = input("Ingrese cambio sexo: ")
    contacto = input("Ingrese cambio contacto: ")
    contacto_emergencia = input("Ingrese cambio contacto emergencia: ")
    direccion = input("Ingrese cambio direccion: ")
    tipo_sangre = input("Ingrese cambio tipo de sangre: ")
    anotaciones = input("Ingrese cambio anotaciones: ")

    print(f"RUT: {id_paciente}, Nombre nuevo: {nombre_s}, Apellido nuevo: {apellido_s}, Edad nueva: {edad}, Nuevo sexo: {sexo}, Contacto nuevo: {contacto}, nuevo contacto emergencia: {contacto_emergencia}, nueva direccion: {direccion}, cambio tipo de sangre: {tipo_sangre}, cambio anotaciones: {anotaciones}")
    
    post = str({'id_paciente': id_paciente, 'nombre_s': nombre_s, 'apellido_s': apellido_s, 'edad': edad, 'sexo': sexo, 'contacto': contacto, 
    'contacto_emergencia': contacto_emergencia, 'direccion': direccion, 'tipo_sangre': tipo_sangre, 'anotaciones': anotaciones}).replace("'",'"').encode()
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5007)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(65507)
            amount_received += len(data)
            print('received {!r}'.format(data))
            return int(data.decode("utf-8"))
    finally:
        print('closing socket')
        sock.close()
