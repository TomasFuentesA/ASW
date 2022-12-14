import socket, sys, json
import os
from db import get_db
import hashlib


database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 8600)
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
#           print('received {!r}',data)

            m = hashlib.sha256()
            pw = bytes(data["pw"],'UTF-8')
            m.update(pw)
            data["pw"] = m.hexdigest()
#           print(data["pw"])

            cursor = database.cursor()
            statement = "SELECT id_cuenta, flag_contrasena FROM cuenta WHERE correo = '" + data["usuario"] + "' AND contrasena = '"+data["pw"]+"';" #Solo select flag
            cursor.execute(statement)
            posts = cursor.fetchone()
            print(posts)
            if posts == None:
                print('Correo o contraseña incorrecta', client_address)
                break
            else:
                print('Envío de datos al cliente')
                list_post = [str(i) for i in posts]
                list_post =  ' '.join(list_post)
                print(list_post)
                connection.sendall(list_post.encode())
                break
    finally:
        connection.close()      