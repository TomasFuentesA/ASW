import socket, sys, json
import os
from db import get_db
import hashlib


database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 6965)
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
            try:
                cursor = database.cursor()
                if data["contacto"] == '':
                    data["contacto"] = 0
                if data["contacto_emergencia"] == '':
                    data["contacto_emergencia"] = 0
                if data["tipo_sangre"] == '':
                    data["tipo_sangre"] = 0
                statement = "INSERT INTO paciente (id_paciente,nombre_s, apellido_s, edad, sexo, contacto, contacto_emergencia, direccion, tipo_sangre, anotaciones) VALUES (?,?,?,?,?,?,?,?,?,?);" #Solo select flag
                cursor.execute(statement,[data["id_paciente"],data["nombre_s"],data["apellido_s"],int(data["edad"]),int(data["sexo"]),int(data["contacto"]),int(data["contacto_emergencia"]),data["direccion"],int(data["tipo_sangre"]),data["anotaciones"]])
                database.commit()
                print('Envío de datos al cliente')
                connection.sendall(str(1).encode())
                break
            except:
                print('Ingreso de paciente erroneo', client_address)
                connection.sendall(str(-1).encode())
                break
    finally:
        connection.close()  