def count_unique(L):
    L2 = []
    for i in L:
        if i not in L2:
            L2.append(i)
    return len(L2)

def remove_duplicates(L):
    L2 = []
    for i in L:
        if i not in L2:
            L2.append(i)
    return L2

def flatten(L):
    L2 = []
    for i in L:
        if isinstance(i, list):
            L2 += flatten(i)
        else:
            L2.append(i)
    return L2

def flatten_rec(L):
    return [i for i in flatten(L)]
