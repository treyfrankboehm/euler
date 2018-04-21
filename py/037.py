#!/usr/bin/env python

from euler import isPrime

def truncPrime(number):
    number = str(number)
    length = len(number)
    for i in range(length):
        if not isPrime(int(number[:i+1])): return False
    for i in range(length-1, 0, -1):
        if not isPrime(int(number[i:])): return False
    return True

sum = 0
total = 0
count = 10
while total < 11:
    if truncPrime(count): sum += count; total += 1
    count += 1
print(sum)

