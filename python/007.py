#!/usr/bin/env python

from euler import isPrime

count = 0
x = 2
while True:
    if isPrime(x) == True: count += 1
    if count == 10001: print x; break
    x += 1
