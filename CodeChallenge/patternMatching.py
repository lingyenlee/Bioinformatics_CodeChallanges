def PatternMatch(Pattern):
    """ return the 1st position of every pattern appearance in genome"""
    f = open("Vibrio_cholerae.txt", "r")
    Genome = f.read()
    pattern_position = []
    x = len(Pattern)
    y = len(Genome)
    for i in range(0, y-x+1):
        if Pattern == Genome[i:i+x]:
            pattern_position.append(str(i))

    print(' '.join(pattern_position))


PatternMatch("CTTGATCAT")
