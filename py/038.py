#!/usr/bin/env python

from euler import isPandigital

def multiples(number):
    numbers = [0]
    for i in range(2,6):
        n = ""
        for j in range(1,i):
            n += str(number * j)
        if isPandigital(n): numbers.append(int(n))
    return max(numbers)

highest = 0
count = 0
while count < 10**4:
    n = multiples(count)
    if n > highest: highest = n
    count += 1
print(highest)

