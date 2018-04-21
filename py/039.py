#!/usr/bin/env python

def hyp(leg1, leg2):
    c = (float(leg1**2) + leg2**2)**.5
    if c % 1 != 0.0: return 1000
    return int(c)

hyps = []
for a in range(1,500):
    for b in range(1,a):
        t = a + b + hyp(a, b)
        if t <= 1000: hyps.append(t)

print(max(set(hyps), key=hyps.count))

