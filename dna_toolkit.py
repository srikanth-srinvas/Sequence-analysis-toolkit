# DNA Toolkit file
import collections

NUCLEOTIDES = ["A", "C", "G", "T"] 

def validate_seq(dna_seq):
    """Validate a DNA sequence.

    Args:
        dna_seq (str): Input DNA sequence to validate.

    Returns:
        str or False: Validated DNA sequence or False if invalid.
    """
    tmp_seq = dna_seq.upper()
    for nuc in tmp_seq:
        if nuc not in NUCLEOTIDES:
            return False
    return tmp_seq

def count_nuc_frequency(seq):
    """Count the frequency of nucleotides in a DNA sequence.

    Args:
        seq (str): Input DNA sequence.

    Returns:
        dict: Dictionary with nucleotide frequencies.
    """
    return dict(collections.Counter(seq))

if __name__ == "__main__":
    # Creating a random DNA sequence for testing:
    rand_dna_str = ''.join(random.choice(NUCLEOTIDES) for _ in range(50))

    dna_str = validate_seq(rand_dna_str)
    if dna_str:
        print("Valid DNA Sequence:", dna_str)
        print("Nucleotide Frequencies:", count_nuc_frequency(dna_str))
    else:
        print("Invalid DNA Sequence!")