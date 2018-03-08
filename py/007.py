#!/usr/bin/env python

from euler import isPrime

num = 0
i = 0
while i < 10001:
    num += 1
    if isPrime(num):
        # Only increment counter if the number is prime
        i += 1

print(num)

