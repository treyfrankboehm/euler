#!/usr/bin/env python

def isPalindromic(number):
	number = str(number)
	if number == number[::-1]: return True
	return False

def toBinary(number):
	total = ""
	length = len(str(number))
	while number > 0:
		total += str(number % 2)
		number = number / 2
	return total[::-1]


total = 0
count = 0
while count < 1000000:
	if isPalindromic(count):
		if isPalindromic(toBinary(count)):
			total += count
	count += 1
print total
