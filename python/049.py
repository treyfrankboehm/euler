#!/usr/bin/env python

from euler import isPrime
from itertools import permutations

primes = [prime for prime in range(1488,10000) if isPrime(prime)]

def isPermutation(x, y, z):
    x = str(x); y = str(y); z = str(z)
    p = [''.join(item) for item in list(permutations(x))]
    if y in p and z in p: return True
    return False

for x in primes:
    y = x + 3330
    if isPrime(y):
        z = y + 3330
        if isPrime(z):
            if isPermutation(x, y, z):
                print str(x) + str(y) + str(z)
                break
