import socket, pickle
import sys, json


def agregar_paciente():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nombre_s = input("Ingrese nombre: ")
    apellido_s = input("Ingrese apellido: ")
    edad = input("Ingrese edad: ")
    sexo = input("Ingrese sexo: ")
    contacto = input("Ingrese contacto (opcional): ")
    contacto_emergencia = input("Ingrese contacto de emergencia (opcional): ")
    direccion = input("Ingrese direccion (opcional): ")
    tipo_sangre = input("Ingrese tipo de sangre (opcional): ")
    anotaciones = input("Ingrese anotaciones (opcional): ")

    post = str({'nombres_s': nombre_s, 'apellido_s' : apellido_s, 'edad' : edad, 'sexo' : sexo, 'contacto' : contacto, 'contacto_emergencia' : contacto_emergencia, 'direccion': direccion,'tipo_sangre' : tipo_sangre,'anotaciones': 
    anotaciones}).replace("'",'"').encode()
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 5015)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(4096)
            amount_received += len(data)
            print('received {!r}'.format(data))

            datos = list(data.decode("utf-8").split(" "))
            print(datos[0])
            return "paciente creado"
    finally:
        print('closing socket')
        sock.close()
