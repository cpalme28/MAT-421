def is_even(p):

    if len(p) == 1:
        return True

    trans = 0

    for i in range(0,len(p)):
        j = i + 1

        for j in range(j, len(p)):
            if p[i] > p[j]: 
                trans = trans + 1

    return ((trans % 2) == 0)