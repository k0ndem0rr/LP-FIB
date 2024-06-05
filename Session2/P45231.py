def fibs():
    a = 0
    yield a
    b = 1
    while True:
        yield b
        a, b = b, a + b

def roots(x):
    a = x
    yield a
    while True:
        a = 0.5 * (a + x / a)
        yield a

def primes():
    yield 2
    n = 3
    yield n
    primes = [2,3]
    while True:
        n += 2
        for p in primes:
            if n % p == 0:
                break
        else:
            primes.append(n)
            yield n

def hammings():
    h = [1]
    seen = []
    while True:
        n = min(h)
        if n not in seen:
            yield n
            seen.append(n)
            h.append(n * 2)
            h.append(n * 3)
            h.append(n * 5)
        h.remove(n)