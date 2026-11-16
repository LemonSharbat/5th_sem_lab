import os
import socket

SERVER_ADDRESS = ("localhost", 8888)
BUFFER_SIZE = 1024

# Create an IPv4 TCP socket and bind it to server address
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)

server_socket.listen(1)
print("Server is listening for incomming connections...")

while True:
    client_socket, client_address = server_socket.accept()

    print("Accepted connection from: ", client_address)

    file_name = client_socket.recv(BUFFER_SIZE).decode()

    print("Requested file:", file_name)

    if os.path.isfile(file_name):

        with open(file_name, "rb") as file:
            file_contents = file.read()

        client_socket.sendall(file_contents)

    else:
        client_socket.sendall(b"File not found")

    client_socket.close()