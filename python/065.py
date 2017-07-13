#!/usr/bin/env python3

import euler

# The continued fraction for e can be expressed as:
#   [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, ... 1, 2k, 1, ...]
# Here we generate a list of such "fraction terms"
fractionTerms = [2, 1, 2]
k = 2
limit = 100
while True:
    fractionTerms.append(1)
    if len(fractionTerms) == limit: break
    fractionTerms.append(1)
    if len(fractionTerms) == limit: break
    fractionTerms.append(2*k)
    if len(fractionTerms) == limit: break
    k += 1

# The first ten terms of the continued fraction expansion are:
#   2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536
#
# Here's a table that links these values together:
#
#   ..................... The previous numerator
#   |                               plus
#   |   ................. The numerator we're manipulating
#   |   |                           times
#   |   |   ............. The current number from fractionTerms
#   |   |   |                       equals
#   |   |   |   ......... The next numerator
#   |   |   |   |
#   pre on  f   new
#   1   2   1   3
#   2   3   2   8
#   3   8   1   11
#   8   11  1   19
#   11  19  4   87
#   19  87  1   106
#   87  106 1   193
#   106 193 6   1264

prev = 0 # Additive identity
on   = 1 # Multiplicative identity
new  = 0 # We don't know this value yet
for i in range(len(fractionTerms)):
    new = prev + on*fractionTerms[i]
    prev, on = on, new

print(euler.sumDigits(new))
