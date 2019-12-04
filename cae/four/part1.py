
matches = 0
for i in range(264360, 746326):
    s = [int(d) for d in str(i)]
    prev = -1
    double = False
    notInc = False
    
    for j in s:
        if j < prev:
            prev = j
            notInc = True
            break
        if j == prev:
            double = True
            
        prev = j

    if double and not notInc:
        matches = matches + 1
            
print(matches)
