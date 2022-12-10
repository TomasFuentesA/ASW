import socket, sys, json
import os
from db import connection
import hashlib


database = connection()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(4096).decode()
            data = json.loads(data)
            print('received {!r}',data)

            cursor = database.cursor()
            statement = "SELECT * FROM cuenta WHERE correo = '" + data["mail"] + "' AND contrasena = '"+data["password"]+"';" #Solo select flag
            cursor.execute(statement)
            if cursor.fetchone() == None:
                print('Correo o contraseña incorrecta', client_address)
                break
            else:
                print('Envío de datos al cliente')
                connection.sendall(cursor.fetchone().encode())
                break
    finally:
        connection.close()        