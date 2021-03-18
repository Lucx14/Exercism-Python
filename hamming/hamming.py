"""Hamming distance calculator"""


def distance(strand_a, strand_b):
    """
    Calculates the hamming distance

    :param strand_a: str
    :param strand_b: str
    :return: int
    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Error: DNA strands must have equal length")

    count = 0

    for nuc_a, nuc_b in zip(strand_a, strand_b):
        if nuc_a != nuc_b:
            count += 1

    return count
