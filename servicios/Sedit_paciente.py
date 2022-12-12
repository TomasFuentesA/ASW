import socket, json
from db import get_db


database = get_db()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5277)
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

        while True:
            data = connection.recv(65507).decode()
            data = json.loads(data)
#           print('received {!r}',data)
            try: 
                if data["id_paciente"] != '':
                    cursor = database.cursor()
                    statement = "UPDATE paciente SET "
                    for key, value in data.items():
                        if value != '':
                            if(key in ["edad", "sexo", "contacto", "contacto_emergencia", "tipo_sangre"]):
                                statement = statement+key+"="+value+","
                            else:
                                statement = statement+key+"='"+value+"',"
                    statement = statement.rstrip(statement[-1]) + " WHERE id_paciente = '"+data['id_paciente']+"'"
                    cursor.execute(statement)
                    database.commit()
                connection.sendall(str(1).encode())
                print("Se modificaron los datos del paciente: ",data["id_paciente"])
                break
            except Exception as e:
                print(e)
                connection.sendall(str(-1).encode())
                print("No se encontró paciente")
                break
    finally:
       connection.close()