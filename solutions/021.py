#!/usr/bin/env python

import euler

total = 0
count = 1
while count < 10000:
	a = sum(euler.factor(count))
	b = sum(euler.factor(a))
	if b == count and a != b: total += a
	count += 1
print total
