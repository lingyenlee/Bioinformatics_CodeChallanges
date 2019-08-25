from hemming import HemmingDistance

def Neighbours(Pattern, d):
    """set of all k-mers pattern with at most d mismatch"""
    if d == 0:
       return Pattern
    if len(Pattern) == 1:
        return ["A", "C", "G", "T"]

    NeighbourHood = set()
    SuffixPattern = Pattern[1:len(Pattern)]
    SuffixNeighbour = Neighbours(SuffixPattern, d)
   
    for text in SuffixNeighbour:
        if HemmingDistance(SuffixPattern, text) < d:
            for x in "ACGT":
                NeighbourHood.add(x+text)
                print("<d",NeighbourHood)
        else:
            NeighbourHood.add(Pattern[0]+text)
    return NeighbourHood

# print(Neighbours("TCCGATACGGA", 3))
print ('\n'.join(map(str, (Neighbours("TCC", 1)))))