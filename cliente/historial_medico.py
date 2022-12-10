import socket, pickle
import sys, json
import time


def historial_medico():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rut = input("Ingrese rut paciente:\n")
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
            #print('received {!r}'.format(data))

            datos = list(data.decode("utf-8").split(" "))
            #print("hola\n")
            print(datos)
            return datos[0], datos[6]
    finally:
        print('closing socket')
        sock.close()
