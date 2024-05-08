from dna_toolkit import *
import random
from utilities import colored

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)
# final print statement with consolidated output 
print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {(colored(transcription(DNAStr)))}\n')

print(colored(reverse_complement(DNAStr)))

# shows the 5' to 3' and 3' to 5' ends of the DNA strands 
print(f"[4] + DNA String + Reverse Complement:\n5' {(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {(colored(reverse_complement(DNAStr)))} 5'\n")

# calculate GC content % for a string and sub sequences with a window si
print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
print(
    f'[6] + GC Content in Subsection k=5: {gc_content_subsec(DNAStr, k=5)}\n')

print(
    f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr, 0)}\n')

print(
    f'[8] + Codon frequency (L): {codon_usage(DNAStr, "L")}\n')


print('[9] + Reading_frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)


test_rf_frame = ['L', 'M', 'T', 'A', 'L', 'V', 'V',
                 'L', 'L', 'R', 'R', 'G', 'S', '_', 'G', 'H']

print(proteins_from_orfs(test_rf_frame))