#!/usr/bin/env python

def isPandigital(number):
	number = str(number)
	if len(number) > 10: return False
	for x in range(10):
		if not str(x) in number: return False
	return True

def subStringDivisibility(number):
	if not isPandigital(number): return 0
	number = str(number)
	if int(number[1:4]) % 2 == 0 and int(number[2:5]) % 3 == 0 and int(number[3:6]) % 5 == 0:
		if int(number[4:7]) % 7 == 0 and int(number[5:8]) % 11 == 0 and int(number[6:9]) % 13 == 0:
			if int(number[7:10]) % 17 == 0:
				return int(number)
	return 0

def makeDivisible(number, factor):
	newNum = ((factor - number)%2)
	if newNum == factor: return 0
	return newNum


#count = "1406357289"
#print count[3], count[4], count[5], count[6], count[7], count[8], count[9]

total = 0
count = 1000000000
while count <= 10000000000:
	count += makeDivisible(int(str(count)[1:4]), 2)*10**6
	count += makeDivisible(int(str(count)[2:5]), 3)*10**5
	count += makeDivisible(int(str(count)[3:6]), 5)*10**4
	count += makeDivisible(int(str(count)[4:7]), 7)*10**3
	count += makeDivisible(int(str(count)[5:8]), 11)*10**2
	count += makeDivisible(int(str(count)[6:9]), 13)*10**1
	count += makeDivisible(int(str(count)[7:10]), 17)*10**0
	total += subStringDivisibility(count)

print total
