import socket, pickle
import sys, json
from cliente.verificar_rut import verificar_rut


def delete_paciente(): #pasar parametro usuario
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        rut = input("Ingrese RUT paciente a eliminar: ")
        if(verificar_rut(rut)):
            print(f"Rut paciente: {rut}")
            post = str({'Usuario': rut}).replace("'",'"').encode()
            print(post)
            
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 5020)
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
                    return int(data.decode("utf-8"))
            finally:
                print('closing socket')
                sock.close()
        else:
            print("Ingrese rut valido")