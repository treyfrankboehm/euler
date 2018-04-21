#!/usr/bin/env python

from euler import factorial

# I had this problem in discrete math. It is equivalent to asking:
# How many binary strings with length 40 containing exactly 20 1s are
# there? This is answered with a binomial coefficient: nChooseK(40, 20)
print(factorial(40)/(factorial(20)*factorial(20)))

