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