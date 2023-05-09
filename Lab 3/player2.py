import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    host = input('Please enter a host: ')
    port = int(input('Please enter a port: '))
    s.connect((host, port))
    print(f"Connected to {host}:{port}")
except ValueError:
    print("Invalid port number. Please enter a valid integer.")
except socket.gaierror:
    print("Invalid host name or address. Please enter a valid hostname or IP address.")
except ConnectionRefusedError:
    print("Connection refused. The server may be unavailable or the port may be closed.")
except Exception as e:
    print("An error occurred:", e)
finally:
    s.close()
