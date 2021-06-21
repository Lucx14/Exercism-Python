def encode(values):
    encoding = []
    for v in values:
        bs = []
        mask = 0
        while not mask or v:
            bs.append(mask | (v & 0x7F))
            v >>= 7
            mask = 0x80
        encoding += reversed(bs)
    return encoding


def decode(encoding):
    if len(encoding) and (encoding[-1] & 0x80):
        raise ValueError("Incomplete encoding")

    v = 0
    vs = []
    for byte in encoding:
        v = (v << 7) | (byte & 0x7F)
        if byte & 0x80 == 0:
            vs.append(v)
            v = 0

    return vs
