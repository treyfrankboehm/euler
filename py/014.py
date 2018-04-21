#!/usr/bin/env python

# Definitely not the most efficient, but it gets it done.

def collatzTerms(number):
    count = 1
    while number != 1:
        if number % 2 == 0:
            number = number/2
            count += 1
        else:
            number = number*3 + 1
            count += 1
    return count

if __name__ == "__main__":
    count   = 1
    collatz = 0
    highestCount   = 0
    highestCollatz = 0
    while count < 1000000:
        collatz = collatzTerms(count)
        if collatz > highestCollatz:
            highestCount   = count
            highestCollatz = collatz
        count += 1
    print(highestCount)

