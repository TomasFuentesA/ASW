import socket, pickle
import sys, json
from cliente.detect_email import detect_email


def Login():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    while True:
        usuario = input("Ingrese Correo: ")
        if (detect_email(usuario)):
            pw = input("Ingrese Password: ")
            #print(f"usuario: {usuario}, Password: {pw}")
            post = str({'usuario': usuario, 'pw': pw}).replace("'",'"').encode()
            
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 7305)
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            try: 
                sock.sendall(post)
                amount_received = 0
                amount_expected = len(post)

                while amount_received < amount_expected:
                    data = sock.recv(4096)
                    amount_received += len(data)
                    #print('received {!r}'.format(data))
                    datos = list(data.decode("utf-8").split(" "))
                    print(datos[0])
                    return datos[0], datos[6]
            finally:
                print('closing socket')
                sock.close()
        else:
            print('Ingrese un correo válido')