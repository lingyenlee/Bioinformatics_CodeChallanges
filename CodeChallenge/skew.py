def MinSkew(sequence):
    """ find the position of given DNA sequence where the min skew occures """
    # initialize all variables
    f = open("dataset_7_6.txt", "r")
    sequence = f.read()
    g = 0
    c = 0
    index = 0
    skew_index = []  # an index array to push index of updated min skew value
    min_skew = 0
    # loop through DNA sequence
    for i in sequence:
        # track index value
        index += 1
        if i == "G":
            g += 1
        if i == "C":
            c += 1
        skew = g - c
        # print(skew)
        if skew < min_skew:
            # update skew index for min skew found
            skew_index = [index]
            # update min skew if it is smaller
            min_skew = skew

        # if min_skew is found, update skew index
        if skew == min_skew and index not in skew_index:
            skew_index.append(index)
    return skew_index


def MaxSkew(sequence):
    """ find the position of given DNA sequence where the max skew occures """
    # initialize all variables
    g = 0
    c = 0
    index = 0
    skew_index = []  # an index array to push index of updated min skew value
    max_skew = 0
    # loop through DNA sequence
    for i in sequence:
        # track index value
        index += 1
        if i == "G":
            g += 1
        if i == "C":
            c += 1
        skew = g - c
        if skew > max_skew:
            # update skew index for max skew found
            skew_index = [index]
            # update max skew if it is bigger
            max_skew = skew

    return skew_index


print("min skew = ",  MinSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"))
print("max skew = ", MaxSkew("GCATACACTTCCCAGTAGGTACTG"))
