
matches = 0
for i in range(264360, 746325+1):
    s = [int(d) for d in str(i)]
    prev = -1
    double = False
    dupe = 0
    notInc = False
    
    for ind, val in enumerate(s):
        if val < prev:
            prev = val
            notInc = True
            break
        if val == prev:
            dupe = dupe + 1
            if ind == len(s) - 1:
                if dupe == 1:
                    double = True
        if val != prev:
            if dupe == 1:
                double = True
            dupe = 0
            
        prev = val

    if double and not notInc:
        matches = matches + 1
            
print(matches)
