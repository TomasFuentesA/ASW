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
            contrasena = input("Ingrese contrasena: ")
            nombre_s = input("Ingrese nombre: ")
            apellido_s = input("Ingrese apellido: ")
            especialidad = input("Ingrese especialidad (opcional): ")
            flag=0
            post = str({'id_cuenta': rut,'correo': correo,'contrasena':contrasena,'nombre_s': nombre_s ,'apellido_s' : apellido_s,  'especialidad' : especialidad, 'flag_contrasena' : flag}).replace("'",'"').encode()
            
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 5030)
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            try: 
                sock.sendall(post)
                amount_received = 0
                amount_expected = len(post)

                while amount_received < amount_expected:
                    data = sock.recv(1000000)
                    amount_received += len(data)
                    print('received {!r}'.format(data))

                    datos = list(data.decode("utf-8").split(" "))
                    print(datos[0])
                    return "cuenta creada"
            finally:
                print('closing socket')
                sock.close()
        else:
            print("Ingrese rut o email válido")
