def NumberToSymbol(num):
    """convery index to symbols """
    if num == 0:
        symbol = "A"
    elif num == 1:
        symbol = "C"
    elif num == 2:
        symbol = "G"
    elif num == 3:
        symbol = "T"
    return symbol

def NumberToPattern(index, k):
    if k==1:
        return NumberToSymbol(index)
    prefixIndex = index // 4
    r = index % 4
    symbol = NumberToSymbol(r)
    print(symbol)
    PrefixPattern = NumberToPattern(prefixIndex, k-1)
    print(PrefixPattern)
    return PrefixPattern + symbol

# print(NumberToPattern(5437, 7))
