#!/usr/bin/env python

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]

count = 1
sundayCount = 1
for year in range(1901, 2001):
    for month in range(0,12):
        day = months[month]
        if month == 1 and year % 4 == 0:
            day += 1
        count += day
        n = days[(count % 7 - 1)]
        if n == "Sun": sundayCount += 1

print sundayCount
