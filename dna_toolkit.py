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

def gc_content(seq):
    # calculates the GC content % in the given sequence 
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


# To calculate the GC content for a specific window of k 
def gc_content_subsec(seq, k=20):
    """GC Content in a DNA/RNA sub-sequence length k. k=20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res

# to translate DNA string into proteins using the codon table
def translate_seq(seq, init_pos=0):
    """Translates a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]

def codon_usage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict

def gen_reading_frames(seq):
    """Generates six reading frames of the given DNA string, including its reverse complement"""
    frames = []
    frames.append(translate_seq(seq,0))
    frames.append(translate_seq(seq,1))
    frames.append(translate_seq(seq,2))
    frames.append(translate_seq(reverse_complement(seq),0))
    frames.append(translate_seq(reverse_complement(seq),1))
    frames.append(translate_seq(reverse_complement(seq),2))
    return frames 

def proteins_from_rfs(aa_seq):
    """Read all possible proteins in an aminoacid string and return a list of possible amino acids which make a protein"""
    current_prot = []
    proteins = []
    for aa in aa_seq:
        if aa == "_":
            # STOP accumulating amino acids if _ - STOP codon is found
            if current_prot:
                for p in current_prot:
                    proteins.append(p)
                current_prot = []
        else:
            # START accumulating amino acids if M start codon is found
            if aa == "M":
                current_prot.append("")
            for i in range(len(current_prot)):
                current_prot[i] += aa
    return proteins

# generate all reading frames
# extract all proteins from RFs
# return a list

def proteins_from_rf(rf):
    """Extract proteins from a given reading frame."""
    # Placeholder for actual implementation
    return []  # Modify this to return actual proteins

def all_proteins_from_orfs(seq, startReadPos=0, endReadPos=0, ordered=False):
    """Compute all possible proteins for all open reading frames"""
    """Protine Search DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2"""
    """API can be used to pull protein info"""
    if endReadPos > startReadPos:
        rfs = gen_reading_frames(seq[startRead: endRead])
    else:
        rfs = gen_reading_frames(seq)

    res = []
    for rf in rfs:
        prots = proteins_from_rf(rf)
        for p in prots:
            res.append(p)

    if ordered:
        return sorted(res, key=len, reverse=True)
    return res