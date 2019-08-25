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

print(ComputingFreq("ACGAATGAGATATGAGATGAATGAGATCAACTATGAGATCTTGGATGAGATATGAGATAAGATGAGATGGAATAGGCATATGAGATCGATGAGATATGAGATACATGAGATATGAGATCTTGACTCTTCTATCATACTCGATATGAGATCATGAGATATGAGATTATGAGATACTATGAGATTAAATGAGATCATCTCCATTATGAGATGATGAGATATAGCATGAGATAATGAGATAAGTCAGTATGAGATCAAGGA", 3))


def FasterFrequentWords(Text, k):
    frequentPattern = set()
    frequentArray = ComputingFreq(Text, k)
    maxKey = max(frequentArray, key=frequentArray.get)
    maxCount = frequentArray[maxKey]
    for i in range(0, (4**k)-1):
        if frequentArray[i] == maxCount:
            pattern = NumberToPattern(i, k)
            frequentPattern.add(pattern)
    return frequentPattern
    
# print(FasterFrequentWords("ACGAATGAGATATGAGATGAATGAGATCAACTATGAGATCTTGGATGAGATATGAGATAAGATGAGATGGAATAGGCATATGAGATCGATGAGATATGAGATACATGAGATATGAGATCTTGACTCTTCTATCATACTCGATATGAGATCATGAGATATGAGATTATGAGATACTATGAGATTAAATGAGATCATCTCCATTATGAGATGATGAGATATAGCATGAGATAATGAGATAAGTCAGTATGAGATCAAGGA", 3))
