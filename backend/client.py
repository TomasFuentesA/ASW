import socket
import sys
import time

def getSize(size):
    while len(size) < 4:
        size = '0' + size
    return size

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5000
sock.connect((host, port))
print('Bienvenido al servicio de autenticación')

while True:
    usuario = input('Ingrese su usuario: ')
    passw = input('Ingrese su contraseña: ')
    service = 'service_example'
    size = len(usuario) + len(passw) + len(service) + 1
    msg = getSize(str(size)) + 'service_example' + usuario + ' ' + passw
    
    sock.send(msg.encode('utf-8'))
    resp = sock.recv(4096)
    print(resp)