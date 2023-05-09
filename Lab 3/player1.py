import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = str(input('Please enter a host: '))
    port = int(input('Please enter a port: '))
    s.bind((host, port))
    s.listen(2)
    print('Waiting for connection')
    c, address = s.accept()
    with c:
        print('Connected by', address)
        while True:
            data = c.recv(1024)
            if not data:
                break
            conn.sendall(data)


