#!/usr/bin/env python

count = 2
total = 0
while count < 1000000:
	if sum([int(x)**5 for x in str(count)]) == count: total += count
	count += 1
print total
