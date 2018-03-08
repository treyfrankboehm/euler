#!/usr/bin/env python

from euler import isPrime

number = 997
while number >= 1:
    if isPrime(number):
        i = 1
        while ((10**i)-1) % number != 0:
            i += 1
        if (number - i) == 1: break
    number -= 2
print(number)
