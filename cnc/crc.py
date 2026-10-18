GENERATOR = [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]


def crc_division(data):
    temp = data.copy()

    for i in range(len(data) - len(GENERATOR) + 1):
        if temp[i] == 1:
            for j in range(len(GENERATOR)):
                temp[i + j] ^= GENERATOR[j]

    return temp[-(len(GENERATOR) - 1):]


def generate_crc(data):
    padded_data = data + [0] * (len(GENERATOR) - 1)
    remainder = crc_division(padded_data)
    return remainder, data + remainder


print("CRC Error Detection")

data = [int(bit) for bit in input("Enter data bits (0/1): ")]

remainder, transmitted_data = generate_crc(data)

print("CRC:", remainder)
print("Transmitted data:", transmitted_data)

received_data = transmitted_data.copy()

choice = input("Introduce error? (Y/N): ").upper()

if choice == "Y":
    position = int(input("Enter bit position to change: "))
    received_data[position - 1] ^= 1

print("Received data:", received_data)

remainder = crc_division(received_data)

if all(bit == 0 for bit in remainder):
    print("No Error")
else:
    print("Error Detected")