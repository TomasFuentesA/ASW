import socket, pickle
import sys, json


def Cambio_pw(Usuario): #pasar parametro usuario
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pw1 = input("Ingrese Password actual: ")
    pw2 = input("Ingrese Password nueva: ")
#   print(f"Password actual: {pw1}, Password nueva: {pw2}")
    post = str({'Usuario': Usuario,'Password': pw1, 'c_Password': pw2}).replace("'",'"').encode()
    
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 7002)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)
    try: 
        sock.sendall(post)
        amount_received = 0
        amount_expected = len(post)

        while amount_received < amount_expected:
            data = sock.recv(4096)
            amount_received += len(data)
#           print('received {!r}'.format(data))
            return int(data.decode("utf-8")), Usuario
    finally:
        print('closing socket')
        sock.close()
