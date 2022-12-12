import socket, sys, json
import os
from db import get_db
import hashlib


database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 7032)
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
            #print('received {!r}',data)
            if data["c_Password"] != '':
                m = hashlib.sha256()
                pw = bytes(data["c_Password"],'UTF-8')
                m.update(pw)
                data["c_Password"] = m.hexdigest()
    #           print(data["c_Password"])
                m = hashlib.sha256()
                pw = bytes(data["Password"],'UTF-8')
                m.update(pw)
                data["Password"] = m.hexdigest()
                print(data["Password"])

                if data["c_Password"] != data["Password"]:
                    cursor = database.cursor()
                    statement = "UPDATE cuenta SET contrasena = '"+data["c_Password"]+"', flag_contrasena = 1 WHERE id_cuenta = '" + data["Usuario"] + "' AND contrasena = '"+data["Password"]+"';" #Solo select flag
                    cursor.execute(statement)
                    database.commit()
                    print('Envío de datos al cliente')
                    connection.sendall(str(-1).encode())
                    break
                else:
                    print('Correo o contraseña incorrecta', client_address)
                    break
            else:
                connection.sendall(str(-2).encode())
                break
    finally:
        connection.close()  