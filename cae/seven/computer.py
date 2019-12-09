#data = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0"
data = "3,8,1001,8,10,8,105,1,0,0,21,30,51,76,101,118,199,280,361,442,99999,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,2,9,9,101,2,9,9,4,9,99,3,9,1002,9,3,9,1001,9,4,9,102,5,9,9,101,3,9,9,1002,9,3,9,4,9,99,3,9,101,5,9,9,102,4,9,9,1001,9,3,9,1002,9,2,9,101,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,3,9,102,5,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99"
#data = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"

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
