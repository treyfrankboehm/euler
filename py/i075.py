#!/usr/bin/env python3

import euler
import math

upperBound = 50
triples = []
sums = []

a = 1.0
while a < upperBound:
    b = 1.0
    aSquared = a**2
    while b < a:
        bSquared = b**2
        c = math.sqrt(aSquared+bSquared)
        if euler.isInt(c):
            triple = sorted([int(a), int(b), int(c)])
            triples.append(triple)
            sums.append(sum(triple))
        b += 1
    a += 1

print(triples)
print((sorted(sums)))
print((sorted(set(sums))))
