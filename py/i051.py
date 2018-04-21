#!/usr/bin/env python3

# Currently broken: yields "2999921" as the answer
# (2090021 is the family)

# for each number:
#   if not prime: pass
#   value = 0
#   primeSum = 0
#   i, j, k = 0
#   three nested loops, each increase by 1 until > len(str(number))
#   at the highest level each time, set index[i], [j], [k] to value
#   test if prime; primeSum += 1
#   primeSum >= 8: print number
#   value += 1

from euler import isPrime

#primes = [x for x in range(1000000) if isPrime(x)]
#print "Primes generated (%d)" % len(primes)

n = 1000
oldN = n
while True:
    oldN += 1
    n = oldN
    if n % 1000 == 0: print(n)
    if not isPrime(n): continue
    value = 0
    oldN = n
    digits = len(str(n))
    primeSum = 0
    i = 1
    while i < digits:
        j = 1
        while j < digits:
            if i == j:
                if j == digits-1:
                    break
                else:
                    j += 1
            k = 1
            while k < digits:
                if k == j or k == i:
                    if k == digits-1:
                        break
                    else:
                        k +=1
                value = 0
                primeSum = 0
                while value < 10:
                    n = list(str(oldN))
                    n[i] = str(value)
                    n[j] = str(value)
                    n[k] = str(value)
                    if isPrime(int(''.join(n))):
                        primeSum += 1
                    if value == 3 and primeSum == 0:
                        break
                    value += 1
                if primeSum == 8:
                    print(n)
                    exit()
                k += 1
            j += 1
        i += 1

