#!/usr/bin/env python3

primes = [2, 3, 5, 7, 11, 13, 17]

def isPandigital(number):
    number = str(number)
    if len(number) != 10: return False
    for x in range(10):
        if not str(x) in number: return False
    return True

def specialProperty(number):
    if not isPandigital(number): return 0

    for i in range(len(primes)-1,-1,-1):
        if not subStringDivisibility(number, i+1, i+4, primes[i]):
            return False
    return True

def subString(number, dig1, dig2):
    number = number // (10**(10-dig2))
    number = number % (10**(dig2-dig1))
    return number

def subStringDivisibility(number, dig1, dig2, factor):
    return (subString(number, dig1, dig2) % factor == 0)

def makeDivisible(number, factor):
    newNum = ((factor - number)%2)
    if newNum == factor: return 0
    return newNum


if __name__ == "__main__":
    total = 0
    count = int(1e9)
    while count <= int(1e10):
        if specialProperty(count):
            total += count

        # Increment by 17 to keep the last 3 digits divisible, unless
        # we're about to wrap around (at 986 -> 1000 instead of 1003)
        if count % 1000 == 986:
            count += 14
        else:
            count += 17

    print(total)

