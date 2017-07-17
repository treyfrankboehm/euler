#!/usr/bin/env python

def oneTwenty(n):
    for x in range(1,21):
        if n % x != 0: return False
    return True

step = 2*3*5*7*11*13*17*19
count = step
while True:
    if oneTwenty(count) == True: print count; break
    count += step
