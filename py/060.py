#!/usr/bin/env python

import euler
import time

#print catPrimes([3,7,109,673])

limit = int(1e4)

numbers    = range(limit)
numbers[1] = 0 # 1 is not prime

n = 2
while n < limit:
    x = 2*n # n is a prime number, but 2n has n as a factor
    while x < limit:
        numbers[x] = 0
        x += n
    # No use in using already-eliminated non-primes
    n += 1
    try:
        while numbers[n] == 0:
            n += 1
    # The last prime under the limit would return an index error
    except:
        continue
numbers[2] = 0; numbers [5] = 0
numbers = filter(lambda a: a != 0, numbers)
print "PRIMES FOUND"

def catPrimes(l):
    for x in l:
        for y in l:
            if x == y: break
#            if not euler.isPrime(int(str(x)+str(y))):
            if not int(str(x)+str(y)) in numbers:
                return False
#            if not euler.isPrime(int(str(y)+str(x))):
            if not int(str(y)+str(x)) in numbers:
                return False
    return True

for a in numbers:
    for b in numbers:
        if a == b: continue
                if not (str(a) + str(b) in numbers) or not (str(b) + str(a) in numbers): continue
        for c in numbers:
            if a == c or b == c: continue
            for d in numbers:
                if a == d or b == d or c == d: continue
                for e in numbers:
                    if a == e or b == e or c == e: continue
                    if d == e: break
                    p = (a,b,c,d,e)
                    if catPrimes(p):
                        print a, b, c, d, e
                        print a+b+c+d+e
                                                exit()
            #print a, b, c, d, e
    print a
