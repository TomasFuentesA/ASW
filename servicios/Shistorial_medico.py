import socket, sys, json
import os
from db import get_db
import hashlib

database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5019)
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
            statement = "SELECT * FROM diagnostico_medico WHERE id_paciente = '" + data["rut"]+"';"
            cursor.execute(statement)
            posts = cursor.fetchall()
            #print(posts)

            if posts == None:
                print('No existe historial', client_address)
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
