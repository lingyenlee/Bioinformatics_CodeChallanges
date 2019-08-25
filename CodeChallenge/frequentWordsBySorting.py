from numberToPattern import NumberToPattern
from patternToNumber import PatternToNumber

def FrequentWordsBySorting(Text, k):
    """Find frequent words by sorting"""
    frequentPatterns = set()
    index_dict = {}
    count_dict = {}
    for i in range(0, len(Text)-k+1):
        pattern = Text[i:i+k]
        index_dict[i] = PatternToNumber(pattern)
        count_dict[i] = 1

    sortedIndex = sorted(index_dict.values())
    for i in range(1, len(Text)-k):
        if sortedIndex[i] == sortedIndex[i-1]:
            count_dict[i] = count_dict[i-1] + 1
    maxCount = max(count_dict, key=count_dict.get)
    maxCountValue = count_dict[maxCount]
    for i in range(0, len(Text)-k+1):
        if count_dict[i] == maxCountValue:
            pattern = NumberToPattern(sortedIndex[i], k)
            frequentPatterns.add(pattern)
    return (frequentPatterns)


print(FrequentWordsBySorting("AAGCAAAGGTGGG", 2))
