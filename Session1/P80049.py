def count_unique(L):
    return len(set(L))

def remove_duplicates(L):
    return list(set(L))

def flatten(L):
    L2 = []
    for i in L:
        if isinstance(i, list):
            L2 += i
        else:
            L2.append(i)
    return L2

def flatten_rec(L):
    L2 = []
    for i in L:
        if isinstance(i, list):
            L2 += flatten_rec(i)
        else:
            L2.append(i)
    return L2