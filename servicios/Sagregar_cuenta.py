import socket, sys, json
import os
from db import get_db
import hashlib


database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 6930)
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
            data = connection.recv(1000000).decode()
            data = json.loads(data)
            print('received {!r}',data)

            m = hashlib.sha256()
            pw = bytes(data["contrasena"],'UTF-8')
            m.update(pw)
            data["contrasena"] = m.hexdigest()
            print(data["contrasena"])

            try:
                cursor = database.cursor()
                statement = "INSERT INTO cuenta (id_cuenta,correo,contrasena, nombre_s,apellido_s,especialidad,flag_contrasena) VALUES (?,?,?,?,?,?,?);" #Solo select flag
                cursor.execute(statement,[data["id_cuenta"],data["correo"],data["contrasena"],data["nombre_s"],data["apellido_s"],data["especialidad"],int(data["flag_contrasena"])])
                database.commit()
                print('Envío de datos al cliente')
                connection.sendall(str(1).encode())
                break
            except:
                print('Ingreso medico erróneo', client_address)
                break
    finally:
        connection.close()  