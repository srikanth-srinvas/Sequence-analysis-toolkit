dna_seq_1 = "TTCGATCCATTG"
dna_seq_2 = "ATCAATCGATCG"

# Loop approach
def hamming_distance_loop(seq_1, seq_2):
    distance = 0
    for position in range(len(seq_1)):
        if seq_1[position] != seq_2[position]:
            distance += 1
    return distance

# Set approach
def hamming_distance_set(seq_1, seq_2):
    nucleotide_set_1 = set([(x, nucleotide) for x, nucleotide in enumerate(seq_1)])
    nucleotide_set_2 = set([(x, nucleotide) for x, nucleotide in enumerate(seq_2)])
    return len(nucleotide_set_1.difference(nucleotide_set_2))

# Zip approach
def hamming_distance_zip(seq_1, seq_2):
    return len([(nucleotide_1, nucleotide_2) for nucleotide_1, nucleotide_2 in zip(seq_1, seq_2) if nucleotide_1 != nucleotide_2])

# Testing the code:
print("Loop Hamming Distance:", hamming_distance_loop(dna_seq_1, dna_seq_2))
print("Set Hamming Distance:", hamming_distance_set(dna_seq_1, dna_seq_2))
print("Zip Hamming Distance:", hamming_distance_zip(dna_seq_1, dna_seq_2))