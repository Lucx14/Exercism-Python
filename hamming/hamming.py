def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Error: DNA strands must have equal length")

    count = 0
    for i, nucleotide in enumerate(strand_a):
        if nucleotide != strand_b[i]:
            count += 1

    return count
