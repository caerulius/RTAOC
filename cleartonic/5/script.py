data_og = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,89,49,225,1102,35,88,224,101,-3080,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1101,25,33,224,1001,224,-58,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,78,23,225,1,165,169,224,101,-80,224,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,101,55,173,224,1001,224,-65,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,2,161,14,224,101,-3528,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1002,61,54,224,1001,224,-4212,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,14,71,225,1101,85,17,225,1102,72,50,225,1102,9,69,225,1102,71,53,225,1101,10,27,225,1001,158,34,224,101,-51,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,102,9,154,224,101,-639,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,226,224,102,2,223,223,1006,224,329,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,108,226,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,389,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,494,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,524,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,539,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,614,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,629,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]
data = data_og[:] # copy

part = 2


if part == 1:
    input = 1
else:
    input = 5



def func_add(code, instruction, pm1, pm2, pm3):
    print("Beginning add %s" % code)
    # get values based on modes
    if pm1 == "0":
        val_1 = data[int(code[1])]
    else:
        val_1 = int(code[1])
        
    if pm2 == "0":
        val_2 = data[int(code[2])]
    else:
        val_2 = int(code[2])
        
    # writes are never immediate, write to last param
#    breakpoint()
    print("Storing add %s at %s" % (val_1+val_2,code[3]))

    data[code[3]] = val_1 + val_2
    

def func_mult(code, instruction, pm1, pm2, pm3):
    print("Beginning mult")
    # get values based on modes
    if pm1 == "0":
        val_1 = data[int(code[1])]
    else:
        val_1 = int(code[1])
        
    if pm2 == "0":
        val_2 = data[int(code[2])]
    else:
        val_2 = int(code[2])
        
    # writes are never immediate, write to last param
    print("Storing mult %s at %s" % (val_1*val_2, code[3]))
    data[code[3]] = val_1 * val_2
def func_input(code, instruction, pm1, pm2, pm3):
        
    print("Storing input %s at %s" % (input,code[1]))
#    breakpoint()
    data[int(code[1])] = input
def func_output(code, instruction, pm1, pm2, pm3):
    if pm1 == "0":
        val_1 = data[int(code[1])]
    elif pm1 == "1":
        val_1 = int(code[1])
    else:
        print("Output error")
    print("Output %s" % val_1)
        
def func_jumptrue(code, instruction, pm1, pm2, pm3):
    print("Beginning jump true")
    if pm1 == "0":
        val_1 = data[int(code[1])]
    else:
        val_1 = int(code[1])
    
    if val_1 == 0:
        pass_flag = False
    else:
        pass_flag = True
        
    if pass_flag:
        if pm2 == "0":
            val_2 = data[int(code[2])]
        else:
            val_2 = int(code[2])
        print("Jumping to pos %s " % val_2)
        return int(val_2)
    else:
        return None
    
def func_jumpfalse(code, instruction, pm1, pm2, pm3):
    print("Beginning jump false")
    if pm1 == "0":
        val_1 = data[int(code[1])]
    else:
        val_1 = int(code[1])
    
    if val_1 != 0:
        pass_flag = False
    else:
        pass_flag = True
        
    if pass_flag:
        if pm2 == "0":
            val_2 = data[int(code[2])]
        else:
            val_2 = int(code[2])
        print("Jumping to pos %s " % val_2)
        return int(val_2)
    else:
        return None
    
def func_lessthan(code, instruction, pm1, pm2, pm3):
    print("Beginning less than")
    if pm1 == "0":
        val_1 = data[int(code[1])]
    else:
        val_1 = int(code[1])
        
    if pm2 == "0":
        val_2 = data[int(code[2])]
    else:
        val_2 = int(code[2])    
    
    if val_1 < val_2:
        num = 1
    else:
        num = 0
        
    data[code[3]] = num
        
def func_equal(code, instruction, pm1, pm2, pm3):
    print("Beginning equal to")
    if pm1 == "0":
        val_1 = data[int(code[1])]
    else:
        val_1 = int(code[1])
        
    if pm2 == "0":
        val_2 = data[int(code[2])]
    else:
        val_2 = int(code[2])    
    
    if val_1 == val_2:
        num = 1
    else:
        num = 0
        
    data[code[3]] = num

    
def func_end():
    pass
    
def perform_function(code):
    instruction_str = str(code[0]).zfill(5)
    
    if len(code) == 4:
        instruction, pm1, pm2, pm3 = instruction_str[3:5], instruction_str[2], instruction_str[1], instruction_str[0]
    elif len(code) == 3:
        instruction, pm1, pm2, pm3 = instruction_str[3:5], instruction_str[2], instruction_str[1], None
    elif len(code) == 2:
        instruction, pm1, pm2, pm3 = instruction_str[3:5], instruction_str[2], None, None
    elif len(code) == 1:
        instruction, pm1, pm2, pm3 = instruction_str[3:5], None, None, None
    
    return_flag = None
    if instruction == "01":
        func_add(code, instruction, pm1, pm2, pm3)
    elif instruction == "02":
        func_mult(code,instruction, pm1, pm2, pm3)
    elif instruction == "03":
        func_input(code,instruction, pm1, pm2, pm3)
    elif instruction == "04":
        func_output(code,instruction, pm1, pm2, pm3)
    elif instruction == "05":
        return_flag = func_jumptrue(code,instruction, pm1, pm2, pm3)
    elif instruction == "06":
        return_flag = func_jumpfalse(code,instruction, pm1, pm2, pm3)
    elif instruction == "07":
        return_flag = func_lessthan(code,instruction, pm1, pm2, pm3)
    elif instruction == "08":
        return_flag = func_equal(code,instruction, pm1, pm2, pm3)
    elif instruction == "99":
        func_end()
    else:
        print("Error on finding function? %s" % instruction)
        print("A" + 1)
        
    if return_flag != None:
        return return_flag
        
        
        
        
        
        
        
num = 0
while num < len(data): 
#while num < 12:
    pos_whole = str(data[num])
    pos = int(pos_whole[-1]) # last digit of instruction
    
    # jumps first
    if pos in [5,6]:
        code = data[num:num+3]
        print(">>>>>>>>>>>> Peforming code %s" % code)
        return_flag = perform_function(code)
        if return_flag != None:
            num = return_flag
        else:
            num += 3   
                    
    elif pos in [0,1,2,7,8]:
        code = data[num:num+4]
        print(">>>>>>>>>>>> Peforming code %s" % code)
        num += 4
        perform_function(code)

    elif pos == 3 or pos == 4:
        code = data[num:num+2]
        print(">>>>>>>>>>>> Peforming code %s" % code)
        num += 2
        perform_function(code)

        
    elif pos_whole == "99":
        code = [data[num]]
        print(">>>>>>>>>>>> Peforming code %s" % code)
        perform_function(code)
        print("Finished on 99")
        num = len(data)
    else:
        print("Unknown opcode %s" % pos_whole)
        break

#
#codes2 = []
#for code in codes:
#    if code[0] == 99:
#        print("Done")
#        break
#    else:
#        # parse each code and get its exact definition
#        instruction_str = str(code[0])
#        instruction_str = instruction_str.zfill(5)
#        instruction = instruction_str[3:]
#        pm1, pm2, pm3= instruction_str[2], instruction_str[1], instruction_str[0] # p = param
#
#        print("Code %s instruction %s mode params: param_1 %s param_2 %s param_3 %s" % (code, instruction, pm1, pm2, pm3))
#        codes2.append([code,instruction,pm1,pm2,pm3])
#
#
#for code in codes2:        
#    perform_function(code[0], code[1], code[2], code[3], code[4])
