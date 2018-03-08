#!/usr/bin/env python

step = 2
on = 1
total = 1
while step < 1001:
    for x in range(4):
        on += step
        total += on
    step += 2
print(total)
