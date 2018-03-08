#!/usr/bin/env python

from euler import factorial

total = 0
for n in range(1,101):
    for r in range(1,n):
        if r > n: break
        c = (factorial(n))/(factorial(r)*factorial(n-r))
        if c > 1000000:
            total += 1
print(total)
