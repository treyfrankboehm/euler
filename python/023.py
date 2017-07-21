#!/usr/bin/env python3

import euler

limit = 28124

nums = []
abundant  = [num for num in range(12,limit) if euler.isAbundant(num)]
print len(abundant)

for a in abundant:
    for b in abundant:
        c = a+b
        if c >= limit:
            break
        nums.append(c)
#    print a
        
nums = list(set(nums))

print(sum(range(limit)) - sum(nums))

