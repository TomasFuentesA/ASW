import socket, sys, json
import os
from db import get_db
import hashlib


database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5020)
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
            print(type(data))
            data = json.loads(data)
            print('received {!r}',data)

            try:
                cursor = database.cursor()
                statement = "DELETE FROM paciente WHERE id_paciente = '" +data["Usuario"]+"';" 
                cursor.execute(statement)
                database.commit()
                print('Envío de datos al cliente')
                connection.sendall(str(-1).encode())
                break
            
            except:
                print("No se encontró paciente")
                break
    finally:
        connection.close()  