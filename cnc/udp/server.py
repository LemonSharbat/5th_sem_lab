import socket


SERVER_ADDRESS = ("localhost", 8888)
BUFFER_SIZE = 1024


# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket to server IP and port
server_socket.bind(SERVER_ADDRESS)

print("UDP server is up and listening...")


while True:

    # Receive expression and client address
    data, client_address = server_socket.recvfrom(BUFFER_SIZE)

    expression = data.decode().strip()

    print("\nEquation from client:", client_address)
    print("Expression:", expression)

    try:
        # Find the operator
        operator = None

        for op in ["+", "-", "*", "/", "%"]:
            if op in expression:
                operator = op
                break

        if operator is None:
            result = "Invalid expression."

        else:
            # Split expression into two numbers
            num1, num2 = expression.split(operator)

            num1 = float(num1)
            num2 = float(num2)

            # Perform operation
            if operator == "+":
                result = num1 + num2

            elif operator == "-":
                result = num1 - num2

            elif operator == "*":
                result = num1 * num2

            elif operator == "/":
                if num2 == 0:
                    result = "Division by zero."
                else:
                    result = num1 / num2

            elif operator == "%":
                if num2 == 0:
                    result = "Division by zero."
                else:
                    result = num1 % num2

    except ValueError:
        result = "Invalid expression."

    print("Result sent to client:", result)

    # Send result back to the client
    server_socket.sendto(
        str(result).encode(),
        client_address
    )