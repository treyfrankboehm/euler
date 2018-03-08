#!/usr/bin/env python

from euler import factorial

def digitFactorial(number):
    total = 0
    number = str(number)
    for digit in number:
        total += factorial(int(digit))
    return total

total = 0
count = 3
while count < 100000:
    if count == digitFactorial(count):
        total += count
    count += 1
print(total)
