#!/usr/bin/env python

"""
one
two
three
four
five
six
seven
eight
nine
ten
eleven
twelve
thirteen
fourteen
fifteen
sixteen
seventeen
eighteen
nineteen
twenty
thirty
fourty
fifty
sixty
seventy
eighty
ninety
hundred
thousand
"""

def oneDigit(number):
    if number == "0": return 0
    if number == "1": return 3
    if number == "2": return 3
    if number == "3": return 5
    if number == "4": return 4
    if number == "5": return 4
    if number == "6": return 3
    if number == "7": return 5
    if number == "8": return 5
    if number == "9": return 4

def twoDigits(number):
    if number == "10": return 3
    if number == "11": return 6
    if number == "12": return 6
    if number == "13": return 8
    if number == "14": return 8
    if number == "15": return 7
    if number == "16": return 7
    if number == "17": return 9
    if number == "18": return 8
    if number == "19": return 8

    number = str(number)
    if number[0] == "2": return 6 + oneDigit(number[1])
    if number[0] == "3": return 6 + oneDigit(number[1])
    if number[0] == "4": return 5 + oneDigit(number[1])
    if number[0] == "5": return 5 + oneDigit(number[1])
    if number[0] == "6": return 5 + oneDigit(number[1])
    if number[0] == "7": return 7 + oneDigit(number[1])
    if number[0] == "8": return 6 + oneDigit(number[1])
    if number[0] == "9": return 6 + oneDigit(number[1])

def threeDigits(number):
    # "hundredand" is 10 characters
    if number[1] == "0":
        if number[2] == "0":
            return oneDigit(number[0]) + 7
        else:
            return oneDigit(number[0]) + 10 + oneDigit(number[2])
    else:
        return oneDigit(number[0]) + 10 + twoDigits(number[1:])

def characters(number):
    if len(str(number)) == 1: return oneDigit(number)
    if len(str(number)) == 2: return twoDigits(number)
    if len(str(number)) == 3: return threeDigits(number)

total = 11 # "onethousand" is 11 characters
for x in range(1,1000):
    total += characters(str(x))
print(total)

