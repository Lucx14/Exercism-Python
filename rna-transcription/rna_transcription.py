def to_rna(dna_strand):
    NUCLEOTIDE_MAP = str.maketrans("ACGT", "UGCA")
    return dna_strand.translate(NUCLEOTIDE_MAP)
