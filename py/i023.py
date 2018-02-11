#!/usr/bin/env python

from euler import factor

max = 28123

def isAbundant(number):
    return sum(factor(number)) > number

abundantNumbers = [x for x in range(12,max) if isAbundant(x)]
abundantCount = len(abundantNumbers)
print abundantCount
print "Abundant numbers found"

"""
numbers = []
a = 0; i = 0
while i < abundantCount:
    j = 0
    while j < abundantCount:
        c = abundantNumbers[i] + abundantNumbers[j]
        if c > max: break
        numbers.append(c)
        j += 1
    i += 1
    print i
"""

numbers = [x for x in range(28123)]

a = 0
while a < max:
    j = 0
    while j < abundantCount:
        i = a - abundantNumbers[j]
        if i < 0: break
        if isAbundant(i):
            numbers[i] = 0
            break
        j += 1
    a += 1

print sum(range(max+1)) - sum(set(numbers))
print sum(set(numbers))
#print set(numbers)
