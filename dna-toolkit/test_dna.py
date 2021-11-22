from dna_lib import *

dna = createSeq(20)

print(f"DNA string :\n {dna}")
print(f"validate DNA string :\n {validateSeq(dna)}")
print(f"count nucleolus frequence :\n {countNucFreq(dna)}")
print(f"transciption :\n {transciption(dna)}")
print(f"compliment :\n {compliment(dna)}")
print(f"reverse complimented : \n {reverse(compliment(dna))}")
print(f"GC rate :\n {gcRate(dna)}")