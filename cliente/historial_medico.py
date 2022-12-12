import socket, pickle
import sys, json
import time
from cliente.verificar_rut import verificar_rut

def historial_medico():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        rut = input("Ingrese rut paciente:\n")
        if(verificar_rut(rut)):
            post = str({'rut': rut}).replace("'",'"').encode()
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 5019)
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            try: 
                sock.sendall(post)
                amount_received = 0
                amount_expected = len(post)

                while amount_received < amount_expected:
                    data = sock.recv(4096)
                    amount_received += len(data)
                    var = data.decode()
                    if len(var) != 0:   
                        print('received {!r}'.format(data))
#                        datos = list(data.decode("utf-8").split(" "))
                        return
                    else:
                        print('No existe historiall')
                        return
            finally:
                print('closing socket')
                sock.close()
        else:
            print("Ingrese rut valido")