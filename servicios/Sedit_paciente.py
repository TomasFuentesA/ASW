import socket, sys, json
import os
from db import get_db
import hashlib


database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5007)
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

        # Verificar ultima coma, cambiar nombre de parametros a los de la DB, verificar tipos de datos en el ingreso, terminar update.
        while True:
            data = connection.recv(65507).decode()
            data = json.loads(data)
            print('received {!r}',data) 
            if data["RUT"] != '':
                cursor = database.cursor()
                statement = "UPDATE paciente SET "
                for key, value in data.items():
                    if value != '':
                        if key == "anotaciones":
                            statement = statement+key+"="+value+' '
                        else:
                            statement = statement+key+"="+value+', '
                statement = statement + 'WHERE id_paciente = '+data['RUT']
            print(statement)
    finally:
       connection.close()
'''
                cursor.execute(statement)
                database.commit()
                print('Envío de datos al cliente')
                connection.sendall(str(-1).encode())
                break
            else:
                print('Debe ingresar Rut del paciente', client_address)
                break
'''