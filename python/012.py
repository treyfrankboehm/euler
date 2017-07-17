#!/usr/bin/env python

from euler import *

count = 0
step = 1
while True:
    count += step
    step += 1
    if len(factor(count)) >= 500: print count; break
