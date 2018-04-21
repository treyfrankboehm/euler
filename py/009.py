#!/usr/bin/env python

for b in range(1,1000):
    for a in range(1,1000):
        c = (a**2 + b**2)**.5
        if a + b + c == 1000:
            print(int(a*b*c))
            exit()

