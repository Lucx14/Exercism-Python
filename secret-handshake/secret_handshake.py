handshake = {1: "wink", 2: "double blink", 4: "close your eyes", 8: "jump"}


def commands(number):
    sequence = [value for key, value in handshake.items() if number & key]

    if number & 16:
        sequence.reverse()

    return sequence
