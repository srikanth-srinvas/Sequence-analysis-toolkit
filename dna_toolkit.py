import collections
from structures import *

# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    # return dict(collections.Counter(seq))

def transcription(seq):
    # DNA to RNA transcription 
    return seq.replace("T", "U")


def reverse_complement(seq):
    # swaps adenine for thymine and Guanine for Cytosine and vice-versa 
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]
# Pythonic approach 
# mapping = str.maketrans('ATCG', 'TAGC')
# return seq.translate(mapping)[::-1]