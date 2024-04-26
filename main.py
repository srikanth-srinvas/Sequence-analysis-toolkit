from dna_toolkit import *
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(randDNAStr)
# final print statement with consolidated output 
print(f'\nSequence: {(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print((f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
