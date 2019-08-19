def HemmingDistance(a, b):
    count = 0
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return count


def Count(Text, Pattern, d):
    """ given strings Text and Pattern, integer d, return the number of
    occurrences of pattern in text with at most d mismatched """
    # f = open("dataset_9_4.txt", "r")
    # Text = f.read()
    count = 0
    # mismatch_index = []
    for i in range(0, len(Text)-len(Pattern)+1):
        Pattern_2 = Text[i:i+len(Pattern)]
        # print(Pattern_2, len(Pattern_2))
        if HemmingDistance(Pattern, Pattern_2) <= d:
            # mismatch_index.append(str(i))
            count += 1
    # print(' '.join(mismatch_index))
    print(count)
Count("TTGCGCCGATGTGGTGGACTGATTTCCTTCTACGGTCCTTCGGATTGTCAGCCTCCGTGCTTATATTTGGTTACTGTTAAAAATTAGTCTCAGACAAACGGAAGCCGGGCAGAGGTATATAGCGCTGATGGCCATGACGTTTCGGCTCTTTATCGATAGAAATTTTAAATAAAAGAACGAAATGCGGGACCATTTCATAGGGAAAGTGGACTATGACGTGGCCTCTGTGGATCGGTTGGAGGATCGCTTTTCTTTAGCTGGTGTAAAGACGAGACCAACACGCGTAGCCCAAGGTCGCTGCGTCCCCAACGATCCGAACATC","CCTTCT", 3)