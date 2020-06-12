# DNA Functions file

Nucleotides = [ "A", "C", "G", "T"]

# Check the sequence to make sure it is a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


# Creating a random DNA sequence for testing:
import random
randDNAStr = ''.join([random.choice(Nucleotides)
                for nuc in range(50)])


# Frequency
def countNucFrequency(seq):
    tmpFreqDict = { "A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
