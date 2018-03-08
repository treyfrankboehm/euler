#!/usr/bin/env python

# Pretty inefficient

from euler import factor, isPrime

count = 1
while 1:
    f1 = map(isPrime, factor(count)).count(True)
    f2 = map(isPrime, factor(count+1)).count(True)
    f3 = map(isPrime, factor(count+2)).count(True)
    f4 = map(isPrime, factor(count+3)).count(True)
    if f1 >= 4 and f2 >= 4 and f3 >= 4 and f4 >= 4:
        print(count)
        break
    count += 1
