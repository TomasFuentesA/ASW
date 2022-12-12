import socket, pickle
import sys, json
from datetime import date
from cliente.verificar_rut import verificar_rut

#El personal de salud, podrá guardar registro de las atenciones con sus pacientes. 
#Registrando datos como diagnóstico, tratamiento y fecha. 
#En caso de que algún parámetro no se encuentre o esté erróneo, el sistema se encargará de avisar.


def Agregar_diagnostico(id_cuenta):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        rut = str(input("Ingrese Rut Paciente:\n"))
        if(verificar_rut(rut)):
            diagnostico = str(input("Ingrese Diagnostico:\n"))
            tratamiento = str(input("Ingrese Tratamiento:\n"))
            adicional = str(input("Ingrese Informacion Adicional:\n"))
            fecha = str(date.today())

            #print(f"Diagnostico: {diagnostico} \nTratamiento: {tratamiento}")
            post = str({'Diagnostico': diagnostico, 'Tratamiento': tratamiento, 'Fecha': fecha, 'id_cuenta': id_cuenta, 'id_paciente': rut, 'adicional': adicional}).replace("'",'"').encode()
#           print(post)
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 5009)
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            try: 
                sock.sendall(post)
                amount_received = 0
                amount_expected = len(post)

                while amount_received < amount_expected:
                    data = sock.recv(1000000)
                    amount_received += len(data)
#                   print('received {!r}'.format(data))
#                   print(datos[0])

                    return data.decode()
            finally:
                print('closing socket')
                sock.close()
        else:
            print("Ingrese rut valido")
