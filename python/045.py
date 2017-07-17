#!/usr/bin/env python

def isPentagonal(number):
    return (((24*number+1)**.5+1)/6) % 1 == 0.0

total = 0
count = 1
step  = 1
while total < 3:
    if isPentagonal(count):
        total += 1
    step += 4
    count += step
print count
