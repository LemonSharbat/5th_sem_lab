import socket

SERVER_ADDRESS = ("localhost", 8888)
BUFFER_SIZE = 1024

# create TCP socket and connect to server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

file_name = input("Enter file name: ")
client_socket.sendall(file_name.encode())

file_contents = client_socket.recv(BUFFER_SIZE)

if file_contents == b"File not found":

    print("File not found on the server.")

else:

    print("File Contents:")
    print(file_contents.decode())

    # with open("received_" + file_name, "wb") as file:
    #     file.write(file_contents)

    # print("File received successfully.")

client_socket.close()