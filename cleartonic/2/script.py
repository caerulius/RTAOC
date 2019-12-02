data_og = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,13,23,1,23,10,27,1,13,27,31,2,31,10,35,1,35,9,39,1,39,13,43,1,13,43,47,1,47,13,51,1,13,51,55,1,5,55,59,2,10,59,63,1,9,63,67,1,6,67,71,2,71,13,75,2,75,13,79,1,79,9,83,2,83,10,87,1,9,87,91,1,6,91,95,1,95,10,99,1,99,13,103,1,13,103,107,2,13,107,111,1,111,9,115,2,115,10,119,1,119,5,123,1,123,2,127,1,127,5,0,99,2,14,0,0]

def part_1(arg1,arg2):
    data = data_og[:] # copy
    data[1] = arg1
    data[2] = arg2
    num = 0
    codes = []
    while num < len(data):
        pos = data[num]
        if pos == 1 or pos == 2:
            codes.append(data[num:num+4])
            num += 4
        elif pos == 99:
            codes.append([data[num]])
            num += 1
        else:
            print("Unknown opcode %s" % num)
            
    for code in codes:
        if code[0] == 99:
#            print("Done")
            break
        else:
            try:
                num1 = data[code[1]]
                num2 = data[code[2]]
                if code[0] == 1:
                    final = num1 + num2
                elif code[0] ==2:
                    final = num1 * num2
                data[code[3]] = final
            except:
                print("Error on %s" % str(code))
            
    return [data[0],data[1],data[2]]

print("Part 1 success: %s " % part_1(12,2)[0])

def part_2():
    for i in range(100):
        for i2 in range(100):
            run = part_1(i,i2)
            if run[0] == 19690720:
                print("Part 2 success: 100 * noun %s + verb %s = %s" % (run[1],run[2],(run[1]*100)+run[2]))
part_2()