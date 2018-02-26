#!/usr/bin/env python3

names = str(list(open("p022_names.txt")))
# Each name is separated by a 
names = names.split(",")
for i in range(len(names)):
    # Remove quotation marks
    names[i] = names[i][1:-1]
# Remove extra quotation marks from first and last name
names[0] = names[0][2:]
names[-1] = names[-1][:-2]
names.sort()

score = 0
for i in range(len(names)):
    name_score = sum([ord(char)-ord('A')+1 for char in names[i]])
    print(names[i])
    score += name_score * (i+1)

print(score)

