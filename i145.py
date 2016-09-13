total = 0
count = 1
while count < 1000:
    x = str(count + int(str(count)[::-1]))
    if '0' in x or '2' in x or '4' in x or '6' in x or '8' in x: pass
    else: total += 1; print count
    count += 1
print total
