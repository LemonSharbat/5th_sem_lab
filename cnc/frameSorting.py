import random


def divide_message(message, packet_size):
    """Divide the message into fixed-size packets."""

    packets = []

    for i in range(0, len(message), packet_size):
        data = message[i:i + packet_size]

        # Sequence numbers start from 1
        sequence_number = len(packets) + 1

        packets.append((sequence_number, data))

    return packets


def shuffle_packets(packets):
    """
    Shuffle packets to simulate out-of-order arrival.

    Manual implementation using random indices.
    """

    shuffled = packets.copy()

    # Fisher-Yates style shuffling
    for i in range(len(shuffled) - 1, 0, -1):
        j = random.randint(0, i)

        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]

    # Python provides a simpler built-in:
    # random.shuffle(shuffled)

    return shuffled


def sort_packets(packets):
    """
    Sort packets according to their sequence numbers.

    Manual implementation using Bubble Sort.
    """

    sorted_packets = packets.copy()
    n = len(sorted_packets)

    for i in range(n - 1):

        for j in range(n - i - 1):

            # Compare sequence numbers
            if sorted_packets[j][0] > sorted_packets[j + 1][0]:

                sorted_packets[j], sorted_packets[j + 1] = \
                    sorted_packets[j + 1], sorted_packets[j]

    # Python provides a simpler built-in:
    # sorted_packets = sorted(packets, key=lambda packet: packet[0])

    return sorted_packets


def display_packets(packets):
    """Display sequence number and packet data."""

    print("Packet No.\tData")

    for sequence, data in packets:
        print(f"{sequence}\t\t{data}")


def receive_packets(packets):
    """Sort received packets and reconstruct the message."""

    print("\nPackets received:")
    display_packets(packets)

    sorted_packets = sort_packets(packets)

    print("\nPackets after sorting:")
    display_packets(sorted_packets)

    # Extract packet data and combine them
    message = "".join(data for sequence, data in sorted_packets)

    print("\nMessage received:")
    print(message)


# ---------------- MAIN PROGRAM ----------------

message = input("Enter message: ")

packet_size = int(input("Enter packet size: "))

packets = divide_message(message, packet_size)

print("\nFragmented Packets:")
display_packets(packets)

shuffled_packets = shuffle_packets(packets)

receive_packets(shuffled_packets)