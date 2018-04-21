#!/usr/bin/env python

def isPandigital(multiplicand, multiplier, product):
    number = str(multiplicand)+str(multiplier)+str(product)
    if len(number) != 9: return False
    for n in range(1,10):
        if not str(n) in number: return False
    return True

pandigitals = []

for x in range(2500):
    for y in range(1000):
        z = x*y
        if isPandigital(x, y, z) and not z in pandigitals:
            pandigitals.append(z)

print(sum(pandigitals))

