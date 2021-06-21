translation = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": None,
    "UAG": None,
    "UGA": None,
}


def proteins(strand):
    result = []
    codons = [strand[i : i + 3] for i in range(0, len(strand), 3)]

    for codon in codons:
        protein = translation[codon]
        if not protein:
            break
        result.append(protein)

    return result
