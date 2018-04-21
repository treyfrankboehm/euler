#!/usr/bin/env python

def isPrime(n):
    for x in range(2,int(n**.5)+1):
        if n % x == 0: return False
    return True

max = 0
coefs = 0
for a in range(-1000,1000):
    for b in range(-1000,1000):
        n = 0
        while True:
            q = n**2+a*n+b
            if q < 0: break
            if isPrime(q): n += 1
            else: break
            if n > max: max = n; coefs = a*b
print(coefs)

