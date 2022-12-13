import socket, pickle
import sys, json
from cliente.verificar_rut import verificar_rut
from cliente.detect_email import detect_email
def agregar_medico():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        rut = input("Ingrese rut: ")
        correo = input("Ingrese correo: ")
        if(verificar_rut(rut) and detect_email(correo)):
            while True:
                contrasena = input("Ingrese contrasena: ")
                nombre_s = input("Ingrese nombre: ")
                apellido_s = input("Ingrese apellido: ")
                if contrasena != '' and nombre_s != '' and apellido_s != '':       
                    especialidad = input("Ingrese especialidad (opcional): ")
                    flag=0
                    if especialidad == '':
                        especialidad = "Medico General"

                    post = str({'id_cuenta': rut.lower(),'correo': correo,'contrasena':contrasena,'nombre_s': nombre_s ,'apellido_s' : apellido_s,  'especialidad' : especialidad, 'flag_contrasena' : flag}).replace("'",'"').encode()
                    
                    # Connect the socket to the port where the server is listening
                    server_address = ('localhost', 6931)
                    print('connecting to {} port {}'.format(*server_address))
                    sock.connect(server_address)
                    try: 
                        sock.sendall(post)
                        amount_received = 0
                        amount_expected = len(post)

                        while amount_received < amount_expected:
                            data = sock.recv(1000000)
                            amount_received += len(data)
                            #                    print('received {!r}'.format(data))

                            datos = list(data.decode("utf-8").split(" "))
                            return datos[0]
                    finally:
                        print('closing socket')
                        sock.close()
                else:
                    print("Uno de los campos es vacíos, por favor rellenelos todos")        
        else:
            print("Ingrese rut o email válido")