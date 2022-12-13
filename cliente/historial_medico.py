import socket, pickle
import sys, json
import time
from cliente.verificar_rut import verificar_rut
from cliente.bar import bar

def historial_medico():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        rut = input("Ingrese rut paciente:\n")
        if(verificar_rut(rut)):
            post = str({'rut': rut.lower()}).replace("'",'"').encode()
            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 5019)
            print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)
            try:
                bar()
                print("{:<15} {:<14} {:<20} {:<20} {:<20} {:<20}".format("Fecha Tratamiento", "Rut Médico", "Nombre Médico", "Diagnostico", "Tratamiento", "Información Adicional")) 
                sock.sendall(post)
                amount_received = 0
                amount_expected = len(post)

                while amount_received < amount_expected:
                    data = sock.recv(4096)
                    amount_received += len(data)
                    var = data.decode()
                    if len(var) != 0:
                        shistorial = var.split(')')
                        for i in shistorial:
                            if i != '':
                                i = i.replace('(', '')
                                lshistorial = list(i.split(","))                            
                                print("{:<15} {:<14} {:<20} {:<20} {:<20} {:<20}".format(lshistorial[6], lshistorial[1], lshistorial[7] + lshistorial[8], lshistorial[3], lshistorial[4], lshistorial[5] ))
                        input("Presione enter para cerrar historial")
#                        datos = list(data.decode("utf-8").split(" "))
                        return
                    else:
                        print('No existe historial')
                        return
            finally:
                print('closing socket')
                sock.close()
        else:
            print("Ingrese rut valido")