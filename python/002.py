#!/usr/bin/env python

a = 1
b = 0
c = 0
total = 0
while a < 4000000:
	c = a
	a += b
	b = c
	if a % 2 == 0:
		total += a
print total
