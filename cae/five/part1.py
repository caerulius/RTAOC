#data = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0"
data = "3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,61,225,101,34,121,224,1001,224,-49,224,4,224,102,8,223,223,1001,224,6,224,1,224,223,223,1101,67,29,225,1,14,65,224,101,-124,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1102,63,20,225,1102,27,15,225,1102,18,79,224,101,-1422,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,20,44,225,1001,69,5,224,101,-32,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1102,15,10,225,1101,6,70,225,102,86,40,224,101,-2494,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,25,15,225,1101,40,67,224,1001,224,-107,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,2,126,95,224,101,-1400,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1002,151,84,224,101,-2100,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,677,677,224,1002,223,2,223,1006,224,329,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,374,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,7,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1008,677,226,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,479,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,107,226,226,224,1002,223,2,223,1006,224,509,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,524,1001,223,1,223,1007,226,226,224,1002,223,2,223,1006,224,539,1001,223,1,223,107,677,677,224,1002,223,2,223,1006,224,554,1001,223,1,223,1107,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,1007,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,107,226,677,224,102,2,223,223,1005,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,629,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,659,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226"
#data = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"

program = [int(x) for x in data.split(',')]

def processInstruction(opcode, parameters, program):
    jump = False
    index = 0

    #add. adds 1 to 2 and stores in 3
    if instruction == 1:
        if parameters[0][1] == 0:
            val1 = program[parameters[0][0]]
        else:
            val1 = parameters[0][0]
        if parameters[1][1] == 0:
            val2 = program[parameters[1][0]]
        else:
            val2 = parameters[1][0]
        program[parameters[2][0]] = val1 + val2
        index = len(parameters) + 1

    #mul. multiplies 1 to 2 and stores in 3
    elif instruction == 2:            
        if parameters[0][1] == 0:
            val1 = program[parameters[0][0]]
        else:
            val1 = parameters[0][0]
        if parameters[1][1] == 0:
            val2 = program[parameters[1][0]]
        else:
            val2 = parameters[1][0]
        program[parameters[2][0]] = val1 * val2
        index = len(parameters) + 1

    #inp. takes raw input and stores in 1
    elif instruction == 3:
        program[parameters[0][0]] = int(input())
        index = len(parameters) + 1

    #out. prints 1
    elif instruction == 4:
        if parameters[0][1] == 0:
            print(program[parameters[0][0]])
        else:
            print(parameters[0][0])
        index = len(parameters) + 1

    #jit. jumps to 2 if 1 is NOT 0
    elif instruction == 5:
        if parameters[0][1] == 0:
            compval = program[parameters[0][0]]
        else:
            compval = parameters[0][0]

        if compval != 0:
            if parameters[1][1] == 0:
                jumpto = program[parameters[1][0]]
            else:
                jumpto = parameters[1][0]
            index = jumpto
            jump = True
        else:
            index = len(parameters) + 1

    #jif. jumps to 2 if 1 is 0
    elif instruction == 6:
        if parameters[0][1] == 0:
            compval = program[parameters[0][0]]
        else:
            compval = parameters[0][0]

        if compval == 0:
            if parameters[1][1] == 0:
                jumpto = program[parameters[1][0]]
            else:
                jumpto = parameters[1][0]
            index = jumpto
            jump = True
        else:
            index = len(parameters) + 1

    #lt. compares 1 to 2. sets 1 to 3 if less than, sets 0 to 3 otherwise
    elif instruction == 7:
        if parameters[0][1] == 0:
            val1 = program[parameters[0][0]]
        else:
            val1 = parameters[0][0]
        if parameters[1][1] == 0:
            val2 = program[parameters[1][0]]
        else:
            val2 = parameters[1][0]

        if val1 < val2:
            program[parameters[2][0]] = 1
        else:
            program[parameters[2][0]] = 0
        index = len(parameters) + 1

    #eq. compares 1 to 2. sets 1 to 3 if equal, sets 0 to 3 otherwise
    elif instruction == 8:
        if parameters[0][1] == 0:
            val1 = program[parameters[0][0]]
        else:
            val1 = parameters[0][0]
        if parameters[1][1] == 0:
            val2 = program[parameters[1][0]]
        else:
            val2 = parameters[1][0]

        if val1 == val2:
            program[parameters[2][0]] = 1
        else:
            program[parameters[2][0]] = 0
        index = len(parameters) + 1

    #end. termination, program instantly halts.
    elif instruction == 99:
        index = -1

    return (index, jump)

def getModeOrZero(opcode, index):
    if index < len(opcode):
        return opcode[index]
    else:
        return 0

index = 0

while index < len(program):
    opcode = [int(x) for x in str(program[index])]
    opcode.reverse()

    instruction = opcode[0]
    
    if instruction == 1 or instruction == 2 or instruction == 7 or instruction == 8:
        parameters = [(program[index+1], getModeOrZero(opcode, 2)), \
                      (program[index+2], getModeOrZero(opcode, 3)), \
                      (program[index+3], 0)]
    if instruction == 3 or instruction == 4:
        parameters = [(program[index+1], getModeOrZero(opcode, 2))]
    if instruction == 5 or instruction == 6:
        parameters = [(program[index+1], getModeOrZero(opcode, 2)), \
                      (program[index+2], getModeOrZero(opcode, 3))]
    if instruction == 9:
        instruction = 99 #this is a shortcut for the opcode
        parameters = []

    indexModifier = processInstruction(instruction, parameters, program)

    if indexModifier[0] == -1:
        break
    else:
        if indexModifier[1] == True:
            index = indexModifier[0]
        else:
            index = index + indexModifier[0]
