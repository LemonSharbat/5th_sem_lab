FLAG = [0, 1, 1, 1, 1, 1, 1, 0]


def bit_stuff(data):
    """Insert 0 after every five consecutive 1s."""
    stuffed = []
    count = 0

    for bit in data:
        stuffed.append(bit)

        if bit == 1:
            count += 1

            if count == 5:
                stuffed.append(0)   # Stuff a 0
                count = 0
        else:
            count = 0

    return stuffed


def bit_destuff(data):
    """Remove the 0 inserted after five consecutive 1s."""
    destuffed = []
    count = 0

    i = 0

    while i < len(data):
        bit = data[i]
        destuffed.append(bit)

        if bit == 1:
            count += 1

            if count == 5:
                # Skip the stuffed 0
                i += 1
                count = 0
        else:
            count = 0

        i += 1

    return destuffed


def sender(data):
    stuffed_data = bit_stuff(data)

    frame = FLAG + stuffed_data + FLAG

    print("Stuffed Data :", stuffed_data)
    print("Sent Frame   :", frame)

    return frame


def receiver(frame):
    # Remove starting and ending flags
    stuffed_data = frame[len(FLAG):-len(FLAG)]

    data = bit_destuff(stuffed_data)

    print("Received Data:", data)

    return data


# ---------------- MAIN PROGRAM ----------------

n = int(input("Enter number of bits: "))

print("Enter", n, "bits:")
data = [int(input()) for _ in range(n)]

frame = sender(data)

receiver(frame)