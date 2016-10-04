#!/usr/bin/env python

from euler import isPrime

count = 1
factors = []
while count < 600851475143**.5:
	if 600851475143 % count == 0 and isPrime(count) == True:
		factors.append(count)
	count += 1
print max(factors)
