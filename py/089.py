#!/usr/bin/env python3

import re

# Open the file into a list
numerals = list(open("p089_roman.txt"))

# Rules on what to replace to minimize each numeral. The order in which
# these are applied matters, so a Python dictionary is insufficient
rules = [
    ("IIII","IV"),
    ("VV","X"),
    ("VIV","IX"),

    ("XXXX","XL"),
    ("LL","C"),
    ("LXL","XC"),

    ("CCCC","CD"),
    ("DD","M"),
    ("DCD","CM")
]

saved = 0
for num in numerals:
    # Check our num against each rule, updating it each time
    for (substr, replace) in rules:
        # Use a regex to check for a suboptimal sequence
        if re.search(substr, num):
            #print("%s: %s -> %s (%s)" % (num, substr, replace,
            #    re.sub(substr, replace, num)))
            # If there is a match, replace
            num = re.sub(substr, replace, num)
            # Update our running total of saved characters
            saved += len(substr)-len(replace)

print(saved)

