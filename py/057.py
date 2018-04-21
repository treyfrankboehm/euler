#!/usr/bin/env python3

# The first ten terms of the continued fraction expansion are:
# 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985

prevNum = 1 # Starts at 1 so that the first numerator is 3
currNum = 1
nextNum = 0
prevDen = 0 # Starts at 0 so that the first denominator is 2
currDen = 1
nextDen = 0
total   = 0
for i in range(1000):
    nextNum = prevNum + currNum*2
    prevNum, currNum = currNum, nextNum

    nextDen = prevDen + currDen*2
    prevDen, currDen = currDen, nextDen
    if len(str(nextNum)) > len(str(currDen)):
        total += 1

print(total)

