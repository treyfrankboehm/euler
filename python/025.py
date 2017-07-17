#!/usr/bin/env python

a = 1
b = 0
oa = 0
count = 1
while True:
    oa = a
    a += b
    b = oa
    count += 1
    if len(str(a)) >= 1000: print count; break
