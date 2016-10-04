#!/usr/bin/env python

# Module useful for Project Euler

def collatz(number):
	if number == 1: return 1
	if number % 2 == 0: return 1 + collatz(number/2)
	else:
		return 1 + collatz(number*3+1)

def isAbundant(number):
	return number < sum(factor(number))

def isAmicable(a, b):
	if sum(factor(a)) == b and sum(factor(b)) == a: return True
	return False

def isPandigital(number, n=9):
	number = str(number)
	if len(number) != n: return False
	for x in range(1, n+1):
		if not str(x) in number: return False
	return True

def isPerfect(number):
	if number == sum(factor(sum(factor(number)))): return True
	return False

def isPrime(number):
	if number == 0 or number == 1: return False
	if number == 2: return True
	factor = 2
	while factor <= (number**.5+1):
		if number % factor == 0:
			return False
		factor += 1
	return True

def factor(number):
	factors = [1]
	factor1 = 2
	while factor1 <= (number**.5):
		if number % factor1 == 0:
			factor2 = number / factor1
			factors.append(factor1)
			if factor1 != factor2:
				factors.append(factor2)
		factor1 += 1
	return factors

def factorial(number):
	if number == 0: return 1
	return number*(factorial(number-1))


def shellSort(a):
	gaps = [701, 301, 132, 57, 23, 10, 4, 1]

	n = len(a)
	for gap in gaps:
		i = gap
		while i < n:
			temp = a[i]
			j = i
			while j >= gap and a[j-gap] > temp:
				a[j] = a[j-gap]
				j-=gap
			a[j] = temp
			i+=1
	return a
