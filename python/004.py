#!/usr/bin/env python3

def isPalindrome(n):
	n = str(n)
	if n[::-1] == n: return True
	return False

largest = 0
for x in range(100,1000):
	for y in range(100,1000):
		z = x*y
		if isPalindrome(z) == True and z > largest: largest = z

print(largest)

