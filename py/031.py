#!/usr/bin/env python

total = 1
one = 0
while one <= 200:
    two = 0
    while two <= 200:
        if one+two*2 > 200: break
        five = 0
        while five <= 50:
            if one+two*2+five*5 > 200: break
            ten = 0
            while ten <= 20:
                if one+two*2+five*5+ten*10 > 200: break
                twenty = 0
                while twenty <= 10:
                    if one+two*2+five*5+ten*10+twenty*20 > 200: break
                    fifty = 0
                    while fifty <= 4:
                        if one+two*2+five*5+ten*10+twenty*20+fifty*50 > 200: break
                        hundred = 0
                        while hundred <= 2:
                            if one+two*2+five*5+ten*10+twenty*20+fifty*50+hundred*100 > 200: break
                            if one+two*2+five*5+ten*10+twenty*20+fifty*50+hundred*100 == 200: total += 1
                            hundred += 1
                        fifty += 1
                    twenty += 1
                ten += 1
            five += 1
        two += 1
    one += 1

print(total)

