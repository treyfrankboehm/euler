#!/usr/bin/env python3

# All terms in amicable chains _MUST_ be divisible by 2. I can't prove
# this, but I know it to be true intuitively

import euler

limit = int(1e6)

numFacSumArray = [ [n, (1+sum(euler.factor(n)))] for n in range(2,limit,2)]

print("done")

