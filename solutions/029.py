#!/usr/bin/env python

numbers = []
for a in range(2,101):
	for b in range(2,101):
		c = a**b
		if c not in numbers: numbers.append(c)
print len(numbers)
