def myLength(L):
    sum = 0
    for i in L:
        sum += 1
    return sum

def myMaximum(L):
    max = L[0]
    for i in L:
        if i > max:
            max = i
    return max

def average(L):
    sum = 0
    for i in L:
        sum += i
    return sum / myLength(L)

def buildPalindrome(L):
    return L[::-1] + L

def remove(L1, L2):
    L = []
    for i in L1:
        if i not in L2:
            L.append(i)
    return L

def flatten(L):
    L2 = []
    for i in L:
        if isinstance(i, list):
            L2 += flatten(i)
        else:
            L2.append(i)
    return L2

def oddsNevens(L):
    odds, evens = [], []
    for i in L:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return (odds, evens)

def isPrime(n):
    if n < 2: return False
    prime, i = True, 2
    while prime and i < n // 2 + 1:
        prime = n % i != 0
        i += 2 if i > 2 else 1
    return prime

def primeDivisors(n):
    divisors = []
    for i in range(2, n + 1):
        if n % i == 0 and isPrime(i):
            divisors.append(i)
    return divisors
