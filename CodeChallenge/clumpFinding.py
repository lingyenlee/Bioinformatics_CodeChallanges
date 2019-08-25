from numberToPattern import NumberToPattern
from patternToNumber import PatternToNumber


def ComputingFreq(Text, k):
    """ implementing PatternToNumber to find most frequent k-mers pattern """
    frequencyArray = {}
    print("text length", len(Text))
    for i in range(0, (4**k)-1):
        frequencyArray[i] = 0
    
    for i in range(0, len(Text)-k+1):
        pattern = Text[i:i+k]
        j = PatternToNumber(pattern)
        # print(pattern)
        frequencyArray[j] += 1
    
    return frequencyArray

def clumpFinding(Genome, k, t, L):
    """identifies (L,t)-clumps of Genome sequence by finding 
    which k-mers occur at least t times"""
    frequentPatterns = set()
    frequencyArray = {}
    clump = {}
    # initialise an array of clump of length 4^k to 0 
    for i in range(0, (4**k)-1):
        clump[i] = 0
    
    for i in range(0, len(Genome)-L):
        Text = Genome[i:i+L]
        
        frequencyArray = ComputingFreq(Text, k)

        for j in range(0, (4**k)-1):
            if frequencyArray[j] >= t:
                clump[j] = 1
    
    for i in range(0, (4**k)-1):
        if clump[i] == 1:
            pattern = NumberToPattern(i, k)
            frequentPatterns.add(pattern)
    return frequentPatterns

print(clumpFinding("gatcagcataagggtccctgcaatgcatgacaagcctgcagttgttttac", 4, 3,25))
