#!/usr/bin/env python

from fractions import Fraction

def likeDigit(a, b):
    a = str(a); b = str(b)
    if a == b: return 0
    if a[0] == b[0]: return int(a[0])
    if a[1] == b[0]: return int(a[1])
    if a[0] == b[1]: return int(a[0])
    if a[1] == b[1]: return int(a[1])
    else: return 0


def cancelLikeDigits(a, b):
    digit = str(likeDigit(a, b))
    a = str(a); b = str(b)

    if a.index(digit) == 0: a = a[1]
    else: a = a[0]
    if b.index(digit) == 0: b = b[1]
    else: b = b[0]

    try: return float(a)/float(b)
    except: return 0


nums = 1
dens = 1
for num in range(10,100):
    for den in range(99,9,-1):
        if num >= den: break
        if likeDigit(num, den) == 0: continue
        try:
            if cancelLikeDigits(num, den) == float(num)/float(den): nums *= num; dens *= den
        except:
            pass

f = list(str(Fraction(nums, dens)))
print(''.join(f[f.index('/')+1:]))
