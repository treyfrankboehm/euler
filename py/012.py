#!/usr/bin/env python

from euler import factor

num = 1
step = 2
while len(factor(count)) < 500:
    num += step
    step += 1

print(num)

