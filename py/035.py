#!/usr/bin/env python

import euler

def isCircularPrime(number):
    number = str(number)
    for i in range(len(number)):
        if not euler.isPrime(int(number[i:]+number[:i])): return False
    return True

limit = int(1e6)

numbers    = list(range(limit))
numbers[1] = 0 # 1 is not prime

n = 2
while n < limit:
    x = 2*n # n is a prime number, but 2n has n as a factor
    while x < limit:
        numbers[x] = 0
        x += n
    # No use in using already-eliminated non-primes
    n += 1
    try:
        while numbers[n] == 0:
            n += 1
    # The last prime under the limit would return an index error
    except:
        continue

i = 0
while i < limit:
    unprime = list("024568")
    for x in unprime:
        if x in str(numbers[i]):
            numbers[i] = 0
            break
    i += 1

[a for a in numbers if a != 0]

total = 2 # 2 and 5
count = 0
while count < len(numbers):
    if isCircularPrime(numbers[count]): total += 1
    count += 1
print(total)

