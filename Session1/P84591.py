def absValue(x):
    return x if x >= 0 else -x

def power(x, p):
    r = 1
    while p > 0:
        r *= x
        p -= 1
    return r

def isPrime(n):
    if n < 2: return False
    prime, i = True, 2
    while prime and i < n // 2 + 1:
        prime = n % i != 0
        i += 2 if i > 2 else 1
    return prime

def slowFib(n):
    if n < 2: return n
    return slowFib(n - 1) + slowFib(n - 2)

def quickFib(n):
    if n < 2: return n
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b