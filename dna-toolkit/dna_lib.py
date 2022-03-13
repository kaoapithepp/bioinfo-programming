import random

DNA_LABEL = ['A','T','G','C']

DNA_CNT = {
    'A': 0,
    'T': 0,
    'C': 0,
    'G': 0
}

DNA_PAIR = {
    'A' : 'T',
    'G' : 'C',
    'C' : 'G',
    'T' : 'A'
}

DNA_GC = {
    'G' : 0,
    'C' : 0
}

def createSeq(len):
    seq = ''.join(random.choice(DNA_LABEL) for _ in range(len))
    return seq

def validateSeq(seq):
    seq.upper()
    for chk in seq:
        if chk not in DNA_LABEL:
            return False

    return seq

def countNucFreq(seq):
    for curr in seq:
        DNA_CNT[curr] += 1

    return DNA_CNT;

def transciption(seq):
    return seq.replace('T','U')

def compliment(seq):
    comp = ''.join([ DNA_PAIR[nuc] for nuc in seq ])
    return comp

def reverse(seq):
    rev = ''.join(seq[::-1])
    return rev

def gcRate(seq):
    for curr in seq:
        if curr in DNA_GC:
            DNA_GC[curr] += 1
        else:
            pass
    
    return 100 * (DNA_GC['G'] + DNA_GC['C'])/len(seq)