def SymbolToNumber(Symbol):
    """indexing symbols A, C, G, T to index 0, 1, 2, 3 """
    if Symbol == "A":
        number = 0
    elif Symbol == "C":
        number = 1
    elif Symbol == "G":
        number = 2
    elif Symbol == "T":
        number = 3
    return number


def PatternToNumber(pattern):
    """consider the pattern arranging in lexicographically,
    convert pattern to index using recursive"""
    # print(len(pattern))

    if len(pattern) == 0:
        return 0
    symbol = pattern[-1]
    prefix = pattern[0:-1]
    # print("sym", symbol)
    # print("pref",prefix)
    # recursive
    return 4*PatternToNumber(prefix) + SymbolToNumber(symbol)


# print(PatternToNumber("ATG"))  # index at 912


