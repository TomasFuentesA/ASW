import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 5000

sock.connect((host, port))
sock.send(b'00020sinitservice_example')
data = sock.recv(4096)
print(data.decode())
while True:
    data = sock.recv(4096)
    print(data.decode())
    data = data.decode()[10:]
    pos_esp = data.find(' ')
    usuario = data[:pos_esp]
    passw = data[pos_esp + 1:]

    if usuario == 'test_user' and passw == 'admin123':
        print('Usuario autorizado')
        sock.send(b'00026service_exampleautorizado')
    else:
        print('Usuario no autorizado')
        sock.send(b'00029service_exampleno autorizado')