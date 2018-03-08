#!/usr/bin/env python

bigString = ""
count = 0
while count < 10**6:
    bigString += str(count)
    count += 1
p = 1
for i in range(1,7):
    p *= int(bigString[10**i])
print(p)
