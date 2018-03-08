#!/usr/bin/env python

def distance(x1,y1,x2,y2):
    if x1 == x2: return abs(y1 - y2)
    if y1 == y2: return abs(x1 - x2)
    return ((x1 - x2)**2 + (y1 - y2)**2)**.5

def isRight(x1,y1,x2,y2):
    sides = [distance(x1,y1,x2,y2),distance(x1,y1,0,0),distance(0,0,x2,y2)]
    c = max(sides); del sides[sides.index(c)]
    a = sides[0]
    b = sides[1]
    ab2 = (a**2 + b**2)**.5
    if abs(ab2 - c) < .0001: return True
    return False

used = []

number = 20


for x1 in range(number):
    for y1 in range(number):
        for x2 in range(number):
            for y2 in range(number):
                if x2 == 0 and y2 == 0: break
                if x1 == 0 and y1 == 0: break
                point1 = (x1, y1)
                point2 = (x2, y2)
                points = (point1, point2)
                #altpoints = (point2, point1)
#                if point1 != point2 and points not in used and altpoints not in used and isRight(x1,y1,x2,y2): print point1, point2; used.append((point1, point2))
                #if point1 != point2 and points not in used and isRight(x1,y1,x2,y2): print point1, point2; used.append(points)
                if point1 != point2 and points not in used and isRight(x1,y1,x2,y2): used.append(points)
        print(x1)

print(len(used))

