import logging
import itertools
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.StreamHandler()])

#data_input = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
#data_input = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
data_input = [3,8,1001,8,10,8,105,1,0,0,21,30,55,80,101,118,199,280,361,442,99999,3,9,101,4,9,9,4,9,99,3,9,101,4,9,9,1002,9,4,9,101,4,9,9,1002,9,5,9,1001,9,2,9,4,9,99,3,9,101,5,9,9,1002,9,2,9,101,3,9,9,102,4,9,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,101,5,9,9,102,3,9,9,101,3,9,9,4,9,99,3,9,1001,9,2,9,102,4,9,9,1001,9,3,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99]


class IntCode():
    def __init__(self,data):
        self.data = data
        self.terminate = False
        self.position = 0
    
    def func_add(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning add %s" % code)
        # get values based on modes
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        else:
            val_1 = int(code[1])
            
        if pm2 == "0":
            val_2 = self.data[int(code[2])]
        else:
            val_2 = int(code[2])
            
        # writes are never immediate, write to last param
    #    breakpoint()
        logging.debug("Storing add %s at %s" % (val_1+val_2,code[3]))
#        breakpoint()

        self.data[code[3]] = val_1 + val_2
        
    
    def func_mult(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning mult")
        # get values based on modes
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        else:
            val_1 = int(code[1])
            
        if pm2 == "0":
            val_2 = self.data[int(code[2])]
        else:
            val_2 = int(code[2])
            
        # writes are never immediate, write to last param
        logging.debug("Storing mult %s at %s" % (val_1*val_2, code[3]))
        self.data[code[3]] = val_1 * val_2
    def func_input(self,code, instruction, pm1, pm2, pm3):
        input_var = self.input_vars.pop()
        logging.debug("Storing input %s at %s" % (input_var,code[1]))
#        breakpoint()
        self.data[int(code[1])] = input_var
        

        
    def func_output(self,code, instruction, pm1, pm2, pm3):
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        elif pm1 == "1":
            val_1 = int(code[1])
        else:
            logging.debug("Output error")
        self.output = val_1
        logging.debug("Output %s" % val_1)
            
    def func_jumptrue(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning jump true")
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        else:
            val_1 = int(code[1])
        
        if val_1 == 0:
            pass_flag = False
        else:
            pass_flag = True
            
        if pass_flag:
            if pm2 == "0":
                val_2 = self.data[int(code[2])]
            else:
                val_2 = int(code[2])
            logging.debug("Jumping to pos %s " % val_2)
            return int(val_2)
        else:
            return None
        
    def func_jumpfalse(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning jump false")
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        else:
            val_1 = int(code[1])
        
        if val_1 != 0:
            pass_flag = False
        else:
            pass_flag = True
            
        if pass_flag:
            if pm2 == "0":
                val_2 = self.data[int(code[2])]
            else:
                val_2 = int(code[2])
            logging.debug("Jumping to pos %s " % val_2)
            return int(val_2)
        else:
            return None
        
    def func_lessthan(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning less than")
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        else:
            val_1 = int(code[1])
            
        if pm2 == "0":
            val_2 = self.data[int(code[2])]
        else:
            val_2 = int(code[2])    
        
        if val_1 < val_2:
            num = 1
        else:
            num = 0
            
        self.data[code[3]] = num
            
    def func_equal(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning equal to")
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        else:
            val_1 = int(code[1])
            
        if pm2 == "0":
            val_2 = self.data[int(code[2])]
        else:
            val_2 = int(code[2])    
        
        if val_1 == val_2:
            num = 1
        else:
            num = 0
            
        self.data[code[3]] = num
    
        
    def func_end(self):
        pass
        
    def perform_function(self,code):
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
            self.func_add(code, instruction, pm1, pm2, pm3)
        elif instruction == "02":
            self.func_mult(code,instruction, pm1, pm2, pm3)
        elif instruction == "03":
            self.func_input(code,instruction, pm1, pm2, pm3)
        elif instruction == "04":
            self.func_output(code,instruction, pm1, pm2, pm3)
        elif instruction == "05":
            return_flag = self.func_jumptrue(code,instruction, pm1, pm2, pm3)
        elif instruction == "06":
            return_flag = self.func_jumpfalse(code,instruction, pm1, pm2, pm3)
        elif instruction == "07":
            return_flag = self.func_lessthan(code,instruction, pm1, pm2, pm3)
        elif instruction == "08":
            return_flag = self.func_equal(code,instruction, pm1, pm2, pm3)
        elif instruction == "99":
            self.func_end()
        else:
            logging.debug("Error on finding function? %s" % instruction)
            logging.debug("A" + 1)
            
        if return_flag != None:
            return return_flag
            
            
            
            
            
            
    def process_program(self,input_vars):
        self.input_vars = input_vars
        if self.terminate:
            logging.debug ("* Terminate flag set, returning output only*")
            return self.output
        else:
                
            logging.debug ("* Beginning program position %s *" % self.position)

            while self.position < len(self.data): 
            #while num < 12:
                pos_whole = str(self.data[self.position])
                pos = int(pos_whole[-1]) # last digit of instruction
                
                # jumps first
                if pos in [5,6]:
                    code = self.data[self.position:self.position+3]
                    logging.debug(">>>> Peforming code %s" % code)
                    return_flag = self.perform_function(code)
                    if return_flag != None:
                        self.position = return_flag
                    else:
                        self.position += 3   
                                
                elif pos in [0,1,2,7,8]:
                    code = self.data[self.position:self.position+4]
                    logging.debug(">>>> Peforming code %s" % code)
                    self.position += 4
                    self.perform_function(code)
                    
                elif pos == 3:
                    code = self.data[self.position:self.position+2]
                    logging.debug(">>>> Peforming code %s" % code)
                    self.position += 2
                    self.perform_function(code)                    
            
                elif pos == 4:
                    code = self.data[self.position:self.position+2]
                    logging.debug(">>>> Peforming code %s" % code)
                    self.position += 2
                    self.perform_function(code)
                    return self.output
                    
                elif pos_whole == "99":
                    code = [self.data[self.position]]
                    logging.debug(">>>> Peforming code %s" % code)
                    self.perform_function(code)
                    logging.debug("Finished on 99")
                    self.position = len(self.data)
                    self.terminate = True
                    return self.output
    
                else:
                    logging.debug("Unknown opcode %s" % pos_whole)
                    break
    


def part_1():
    max_output = 0
    
    for phases in itertools.permutations(list(range(5))):
        letters = ['A','B','C','D','E']
        alpha = dict(zip(phases,letters))    
        
        output_signal = 0
        for phase_setting, amplifier_name in alpha.items():
            logging.info(">>> Amplifier %s phase_setting %s output_signal %s" % (amplifier_name,phase_setting,output_signal))
            program = IntCode(data_input)
            output_signal = program.process_program([output_signal,phase_setting])
        if output_signal > max_output:
            max_output = output_signal
    print("Max output %s" % max_output)
    
#def part_2():
    
    
max_output = 0

#for phases in itertools.permutations(list(range(5,10))):
for phases in [[9,8,7,6,5]]:
    letters = [['A',IntCode(data_input)],['B',IntCode(data_input)],['C',IntCode(data_input)],['D',IntCode(data_input)],['E',IntCode(data_input)]]
    alpha = dict(zip(phases,letters))
    output_signal = 0
    for phase_setting, amplifier in alpha.items():
        amplifier_name, program = amplifier
        logging.debug(">>> Amplifier %s phase_setting %s output_signal %s" % (amplifier_name,phase_setting,output_signal))
        output_signal = program.process_program([output_signal,phase_setting])
            
    num = 0
    while num < 6:
        for phase_setting, amplifier in alpha.items():

            amplifier_name, program = amplifier
#            if amplifier_name == 'A':
#                breakpoint()
            logging.debug(">>> Amplifier %s phase_setting %s output_signal %s" % (amplifier_name,phase_setting,output_signal))
            output_signal = program.process_program([output_signal])
            if program.terminate == True:
                logging.debug(">>> Terminating loop")
                break
        num +=1
        
    if output_signal > max_output:
        max_output = output_signal
print("Max output %s" % max_output)
