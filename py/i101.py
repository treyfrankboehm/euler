#!/usr/bin/env python3

def fxn(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

for x in range(10):
    print((fxn(x)))
