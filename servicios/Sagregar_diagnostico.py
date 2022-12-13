import socket, sys, json
import os
from db import get_db
import hashlib

database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5009)
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
#           print('received {!r}',data)

            if data:
                cursor = database.cursor()
                statement = "INSERT INTO diagnostico_medico (id_cuenta, id_paciente, diagnostico, informacion_adicional, tratamiento, fecha_diagnostico) VALUES (?,?,?,?,?,?);"
                cursor.execute(statement, [data["id_cuenta"],data["id_paciente"], data["Diagnostico"], data["adicional"], data["Tratamiento"],data["Fecha"]])
                database.commit()
                print('Diagnostico del paciente '+data["id_paciente"]+' agregado correctamente')
                connection.sendall(str(1).encode())
                break
            else:
                print('Ingrese un Diagnostico correcto', client_address)
                connection.sendall(str(-1).encode())
                break
    finally:
        connection.close()  
