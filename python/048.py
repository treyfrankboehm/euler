#!/usr/bin/env python

total = 0
for x in range(1,1001):
	total += x**x
print str(total)[-10:]
