from functools import reduce

def evens_product(L):
    return reduce(lambda x, y: x * (y if y % 2 == 0 else 1), L, 1)

def reverse(L):
    return reduce(lambda x, y: [y] + x, L, [])

def zip_with(f, L1, L2):
    return [f(x, y) for x, y in zip(L1, L2)]

def count_if(f, L):
    return len([x for x in L if f(x)])