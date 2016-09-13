#!/usr/bin/env python3

#   141.py: Solution to Project Euler number 141
#
#   Copyright (c) 2016 Trey Boehm
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more detail.
#   <http://www.gnu.org/licenses/>

# A positive integer, n, is divided by d and the quotient and remainder
# are q and r respectively. In addition d, q, and r are consecutive
# positive integer terms in a geometric sequence, but not necessarily in
# that order.
#
# For example, 58 divided by 6 has quotient 9 and remainder 4. It can
# also be seen that 4, 6, 9 are consecutive terms in a geometric
# sequence (common ratio 3/2).
# 
# We will call such numbers, n, progressive.
#
# Some progressive numbers, such as 9 and 10404 = 1022, happen to also
# be perfect squares. The sum of all progressive perfect squares below
# one hundred thousand is 124657.
#
# TASK: Find the sum of all progressive perfect squares below one
# trillion (10^12).

# ``number'' is ``n'' that is referred to in the problem
# ``dividend'' is ``d''; ``quotient'' is ``q''; ``r'' is remainder
# ``squares'' is a list of square numbers
# isCommonRatio(a, b, c) determines if there is a common ratio between
#   three numbers
# 

squares = [x**2 for x in range(0,100)]


