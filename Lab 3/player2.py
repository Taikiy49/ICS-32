import socket

def connect_to_player1():
    HOST = ''
    PORT = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

def main():
    s = connect_to_player1()

if __name__ == '__main__':
    main()
