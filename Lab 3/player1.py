import socket


def connect_to_player2():
    while True:
        host = input("Enter host name/IP address of Player 2: ")
        port = input("Enter port number to use: ")
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            print("Connected to Player 2.")
            return s
        except:
            print("Could not connect to Player 2.")
            choice = input("Do you want to try again? (y/n): ")
            if choice == 'n':
                return False

