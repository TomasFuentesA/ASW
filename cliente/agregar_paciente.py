import socket, pickle
import sys, json


def agregar_paciente():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rut = input("Ingrese rut: ")
    nombre_s = input("Ingrese nombre: ")
    apellido_s = input("Ingrese apellido: ")
    while True:
        edad = input("Ingrese edad: ")
        sexo = input("Ingrese sexo 1.Masculino 2.Femenino 3.No especifica: ")
        if edad == '' and sexo =='' :
            print("La edad y el sexo no pueden ser vacios")   
        else:
            break    
    contacto = input("Ingrese contacto (opcional): ")
    contacto_emergencia = input("Ingrese contacto de emergencia (opcional): ")
    direccion = input("Ingrese direccion (opcional): ")
    tipo_sangre = input("Ingrese tipo de sangre 1.A+ 2.B+ 3.O+ 4.AB+ 5.A- 6.B- 7.O- 8.AB- (opcional): ")
    anotaciones = input("Ingrese anotaciones (opcional): ")

    post = str({'id_paciente': rut.lower(),'nombre_s': nombre_s, 'apellido_s' : apellido_s, 'edad' : edad, 'sexo' : sexo, 'contacto' : contacto, 'contacto_emergencia' : contacto_emergencia, 'direccion': direccion,'tipo_sangre' : tipo_sangre,'anotaciones': 
    anotaciones}).replace("'",'"').encode()
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 6965)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(1000000)
            amount_received += len(data)
#           print('received {!r}'.format(data))
            return int(data.decode("UTF-8"))
    finally:
        print('closing socket')
        sock.close()
