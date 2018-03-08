#!/usr/bin/env python

from euler import isPrime

primes = [prime for prime in range(10000) if isPrime(prime)]

def goldbach(number):
    for prime in primes:
        for square in range(40):
            if prime + 2*square**2 == number: return True
    return False

count = 9
while 1:
    if not goldbach(count): print(count); break
    count += 2
