#!/usr/bin/env python

def isPentagonal(x):
	return (((24*x+1)**.5+1)/6) % 1 == 0.0

p = [n*(3*n-1)/2 for n in range(1,10000)]

for i in range(len(p)):
	for j in range(i):
		diff = p[i] - p[j]
		sum  = p[i] + p[j]
		if isPentagonal(diff) and isPentagonal(sum):
			print max((p[i]-p[j]), (p[j]-p[i]))
			exit()
