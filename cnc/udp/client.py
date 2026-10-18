import socket


SERVER_ADDRESS = ("localhost", 8888)
BUFFER_SIZE = 1024


# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Read expression from user
expression = input("Enter an expression: ")

# Send expression to server
client_socket.sendto(expression.encode(), SERVER_ADDRESS)

# Receive result from server
result, server_address = client_socket.recvfrom(BUFFER_SIZE)

# Convert bytes to string and display
print(expression, "=", result.decode())

client_socket.close()