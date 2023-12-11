def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    length = 0
    for nucleotide in dna:
        length += 1
    return length


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for base in dna:
        if base == nucleotide:
            count += 1
    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    len_dna2 = get_length(dna2)
    for i in range(get_length(dna1) - len_dna2 + 1):
        if dna1[i:i+len_dna2] == dna2:
            return True
    return False


def is_valid_sequence(sequence):
    """ (str) -> bool

    Return True if the given sequence contains only valid DNA nucleotides
    (A, T, C, G).

    >>> is_valid_sequence('ATCG')
    True
    >>> is_valid_sequence('XYZ')
    False
    """
    valid_nucleotides = {'A', 'T', 'C', 'G'}
    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            return False
    return True


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting dna2 into dna1 at the given
    index.

    >>> insert_sequence('ATCG', 'GGA', 2)
    'ATGGCGA'
    >>> insert_sequence('ATCG', 'GGA', 0)
    'GGATCG'
    """
    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    """ (str) -> str

    Return the complement of a given DNA nucleotide.

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return complements[nucleotide]


def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence's complement.

    >>> get_complementary_sequence('ATCG')
    'TAGC'
    """
    complement_sequence = ''
    for nucleotide in dna:
        complement_sequence += get_complement(nucleotide)
    return complement_sequence
