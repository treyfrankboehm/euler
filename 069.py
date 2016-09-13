#!/usr/bin/env python3

# Generate a list of all primes below (upperLimit)
# Generate another list that contains a list with all numbers below
# (upperLimit) and their prime factors
# Find the longest list

import euler

upperLimit = int(1e6)

primes = [n for n in range(upperLimit)]
divisor = 1
while divisor < upperLimit:
    divisor += 1
    try:
        if primes[divisor] == 0: continue
    except IndexError:
        break
    index = divisor
    while index < upperLimit:
        index += divisor
        try: primes[index] = 0
        except IndexError: break
del primes[1] # 1 is not prime
primes = list(filter((0).__ne__, primes))

numbers = [[n] for n in range(upperLimit)]
divisorIndex = 0
while divisorIndex < len(primes):
    divisor = primes[divisorIndex]
    index = divisor
    while index < upperLimit:
        index += divisor
        try:
            numbers[index].append(divisor)
        except IndexError:
            break
    divisorIndex += 1
del numbers[0] # Having 0 in the list makes it confusing
factorArray = list(filter((0).__ne__, numbers))

bestCount = 0
bestNumber = 0
for number in factorArray:
    count = len(number)
    if count > bestCount:
        bestCount = count
        bestNumber = number[0]

print(bestNumber)
