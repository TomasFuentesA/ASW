import socket, sys, json
import os
from db import get_db
import hashlib


database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5002)
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
            statement = "UPDATE SET cuenta.contrasena = '"+data["c_Password"]+"' * FROM cuenta WHERE id_cuenta = '" + data["Usuario"] + "' AND contrasena = '"+data["Password"]+"';" #Solo select flag
            cursor.execute(statement)
            posts = cursor.fetchone()
            print(posts)
            if posts == None:
                print('Correo o contraseña incorrecta', client_address)
                break
            else:
                print('Envío de datos al cliente')
                list_post = [str(i).encode() for i in posts] 
                connection.sendall(list_post[0])
                break
    finally:
        connection.close()    