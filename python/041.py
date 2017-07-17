#!/usr/bin/env python

import euler

limit = int(1e7)

numbers    = range(limit)
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
filter(lambda a: a != 0, numbers)

print "Primes finally found"

highest = 0
count = 1
while count < limit:
    prime = numbers[count]
    if euler.isPandigital(prime, len(str(prime))):
        highest = count
    count += 1
print highest
