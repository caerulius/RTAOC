import logging
import itertools
logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s %(message)s',
                    handlers=[logging.StreamHandler()])

data_og = [1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1101,3,0,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,1,550,1027,1101,0,0,1020,1101,30,0,1004,1101,0,22,1014,1102,1,36,1009,1101,37,0,1007,1102,25,1,1010,1102,1,33,1012,1102,282,1,1029,1102,1,488,1025,1101,0,31,1019,1101,0,21,1008,1101,0,35,1015,1101,664,0,1023,1102,26,1,1001,1101,28,0,1016,1102,29,1,1005,1102,1,24,1002,1101,20,0,1018,1101,27,0,1013,1101,38,0,1017,1102,1,1,1021,1102,1,557,1026,1102,1,39,1000,1101,23,0,1006,1101,493,0,1024,1102,1,291,1028,1101,671,0,1022,1101,0,34,1003,1101,0,32,1011,109,10,21108,40,40,8,1005,1018,199,4,187,1105,1,203,1001,64,1,64,1002,64,2,64,109,-14,2108,30,8,63,1005,63,225,4,209,1001,64,1,64,1105,1,225,1002,64,2,64,109,3,2102,1,4,63,1008,63,34,63,1005,63,251,4,231,1001,64,1,64,1106,0,251,1002,64,2,64,109,12,2107,22,-5,63,1005,63,269,4,257,1105,1,273,1001,64,1,64,1002,64,2,64,109,20,2106,0,-3,4,279,1001,64,1,64,1106,0,291,1002,64,2,64,109,-16,21108,41,40,-3,1005,1012,311,1001,64,1,64,1105,1,313,4,297,1002,64,2,64,109,-13,2101,0,2,63,1008,63,30,63,1005,63,335,4,319,1105,1,339,1001,64,1,64,1002,64,2,64,109,-3,2102,1,4,63,1008,63,35,63,1005,63,359,1106,0,365,4,345,1001,64,1,64,1002,64,2,64,109,15,1205,6,377,1105,1,383,4,371,1001,64,1,64,1002,64,2,64,109,5,21102,42,1,-2,1008,1017,39,63,1005,63,403,1106,0,409,4,389,1001,64,1,64,1002,64,2,64,109,-17,21107,43,44,10,1005,1012,431,4,415,1001,64,1,64,1106,0,431,1002,64,2,64,109,14,21107,44,43,-4,1005,1012,451,1001,64,1,64,1106,0,453,4,437,1002,64,2,64,109,1,21102,45,1,-3,1008,1014,45,63,1005,63,479,4,459,1001,64,1,64,1105,1,479,1002,64,2,64,109,7,2105,1,0,4,485,1106,0,497,1001,64,1,64,1002,64,2,64,109,5,1206,-8,513,1001,64,1,64,1106,0,515,4,503,1002,64,2,64,109,-33,2101,0,7,63,1008,63,32,63,1005,63,535,1106,0,541,4,521,1001,64,1,64,1002,64,2,64,109,23,2106,0,8,1001,64,1,64,1106,0,559,4,547,1002,64,2,64,109,-1,21101,46,0,-5,1008,1013,46,63,1005,63,585,4,565,1001,64,1,64,1105,1,585,1002,64,2,64,109,-4,21101,47,0,2,1008,1016,44,63,1005,63,605,1105,1,611,4,591,1001,64,1,64,1002,64,2,64,109,-18,1207,4,38,63,1005,63,627,1106,0,633,4,617,1001,64,1,64,1002,64,2,64,109,5,2107,22,7,63,1005,63,649,1106,0,655,4,639,1001,64,1,64,1002,64,2,64,109,12,2105,1,10,1001,64,1,64,1106,0,673,4,661,1002,64,2,64,109,-10,1208,6,33,63,1005,63,693,1001,64,1,64,1106,0,695,4,679,1002,64,2,64,109,-7,2108,35,7,63,1005,63,715,1001,64,1,64,1106,0,717,4,701,1002,64,2,64,109,6,1208,5,37,63,1005,63,735,4,723,1106,0,739,1001,64,1,64,1002,64,2,64,109,-4,1202,5,1,63,1008,63,34,63,1005,63,765,4,745,1001,64,1,64,1105,1,765,1002,64,2,64,109,29,1206,-7,783,4,771,1001,64,1,64,1105,1,783,1002,64,2,64,109,-28,1201,6,0,63,1008,63,29,63,1005,63,809,4,789,1001,64,1,64,1106,0,809,1002,64,2,64,109,5,1202,2,1,63,1008,63,20,63,1005,63,829,1106,0,835,4,815,1001,64,1,64,1002,64,2,64,109,-1,1201,6,0,63,1008,63,35,63,1005,63,859,1001,64,1,64,1105,1,861,4,841,1002,64,2,64,109,2,1207,-3,25,63,1005,63,879,4,867,1105,1,883,1001,64,1,64,1002,64,2,64,109,13,1205,3,901,4,889,1001,64,1,64,1106,0,901,4,64,99,21101,0,27,1,21101,915,0,0,1106,0,922,21201,1,22987,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,0,942,0,1106,0,922,22101,0,1,-1,21201,-2,-3,1,21101,0,957,0,1106,0,922,22201,1,-1,-2,1105,1,968,21202,-2,1,-2,109,-3,2105,1,0]
data_input = data_og[:]
#data_input.extend([0]*10000)

debug_1 = []
debug_2 = []


class IntCode():
    def __init__(self,data):
        self.data = data
        self.terminate = False
        self.position = 0
        self.relative_base = 0
    
    def func_add(self,code, instruction, pm1, pm2, pm3):
#        breakpoint()
        logging.debug("Beginning add %s" % code)
        # get values based on modes
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        elif pm1 == "2":
            val_1 = self.data[self.relative_base + int(code[1])]
        else:
            val_1 = int(code[1])
            
        if pm2 == "0":
            val_2 = self.data[int(code[2])]
        elif pm2 == "2":
            val_2 = self.data[self.relative_base +  + int(code[2])]
        else:
            val_2 = int(code[2])
            
        # writes are never immediate, write to last param
        logging.debug("Storing add %s at %s" % (val_1+val_2,code[3]))
        if pm3 == "2":
            val_3 = self.relative_base + code[3]
        elif pm3 == "0":
            val_3 = code[3]
        else:
            logging.info("ERROR")

        try:
            self.data[val_3] = val_1 + val_2
        except:
            logging.debug("Extending data")
            self.data.extend([0] * ((val_3 - len(self.data))+1))
            try:
                self.data[val_3] = val_1 + val_2
            except:
                breakpoint()
    
    def func_mult(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning mult")
        # get values based on modes
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        elif pm1 == "2":
            val_1 = self.data[self.relative_base + int(code[1])]
        else:
            val_1 = int(code[1])
            
        if pm2 == "0":
            val_2 = self.data[int(code[2])]
        elif pm2 == "2":
            val_2 = self.data[self.relative_base +  + int(code[2])]
        else:
            val_2 = int(code[2])
            
        # writes are never immediate, write to last param
        logging.debug("Storing add %s at %s" % (val_1+val_2,code[3]))
        if pm3 == "2":
            val_3 = self.relative_base + code[3]
        elif pm3 == "0":
            val_3 = code[3]
        else:
            logging.info("ERROR")

        try:
            self.data[val_3] = val_1 * val_2
        except:
            logging.debug("Extending data")
            self.data.extend([0] * ((val_3 - len(self.data))+1))
            try:
                self.data[val_3] = val_1 * val_2
            except:
                breakpoint()
        
    def func_input(self,code, instruction, pm1, pm2, pm3):
        if pm1 == "0":
            address = int(code[1])
        elif pm1 == "2":
            address = self.relative_base + int(code[1])
        else:
            address = int(code[1])

        
        input_var = self.input_vars.pop()
        self.data[address] = input_var
        logging.debug("Storing input %s at %s" % (input_var,address))

        
    def func_output(self,code, instruction, pm1, pm2, pm3):
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        elif pm1 == "2":
            val_1 = self.data[self.relative_base + int(code[1])]
        elif pm1 == "1":
            val_1 = int(code[1])
        else:
            logging.debug("Output error")
        self.output = val_1
        logging.info("Output %s" % val_1)
            
    def func_jumptrue(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning jump true")
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        elif pm1 == "2":
            val_1 = self.data[self.relative_base + int(code[1])]
        else:
            val_1 = int(code[1])
        
        if val_1 == 0:
            pass_flag = False
        else:
            pass_flag = True
            
        if pass_flag:
            if pm2 == "0":
                val_2 = self.data[int(code[2])]
            elif pm2 == "2":
                val_2 = self.data[self.relative_base  + int(code[2])]
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
        elif pm1 == "2":
            val_1 = self.data[self.relative_base + int(code[1])]
        else:
            val_1 = int(code[1])
        
        if val_1 != 0:
            pass_flag = False
        else:
            pass_flag = True
            
        if pass_flag:
            if pm2 == "0":
                val_2 = self.data[int(code[2])]
            elif pm2 == "2":
                val_2 = self.data[self.relative_base + int(code[2])]
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
        elif pm1 == "2":
            val_1 = self.data[self.relative_base + int(code[1])]
        else:
            val_1 = int(code[1])
            
        if pm2 == "0":
            val_2 = self.data[int(code[2])]
        elif pm2 == "2":
            val_2 = self.data[self.relative_base  + int(code[2])]
        else:
            val_2 = int(code[2])
        
        if val_1 < val_2:
            num = 1
        else:
            num = 0
            
        if pm3 == "2":
            self.data[self.relative_base + code[3]] = num
        elif pm3 == "0":
            self.data[code[3]] = num
        else:
            logging.info("ERROR")
            
    def func_equal(self,code, instruction, pm1, pm2, pm3):
        logging.debug("Beginning equal to")
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        elif pm1 == "2":
            val_1 = self.data[self.relative_base + int(code[1])]
        else:
            val_1 = int(code[1])
            
        if pm2 == "0":
            val_2 = self.data[int(code[2])]
        elif pm2 == "2":
            val_2 = self.data[self.relative_base  + int(code[2])]
        else:
            val_2 = int(code[2])
        
        if val_1 == val_2:
            num = 1
        else:
            num = 0
        
        if pm3 == "2":
            self.data[self.relative_base + code[3]] = num
        elif pm3 == "0":
            self.data[code[3]] = num
        else:
            logging.info("ERROR")
    
    def func_relative_base(self,code,instruction, pm1, pm2, pm3):
        logging.debug("Beginning relative base change")
        if pm1 == "0":
            val_1 = self.data[int(code[1])]
        elif pm1 == "2":
            val_1 = self.data[self.relative_base + int(code[1])]
        else:
            val_1 = int(code[1])
            
        self.relative_base = self.relative_base + val_1

        
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
        elif instruction == "09":
            return_flag = self.func_relative_base(code,instruction, pm1, pm2, pm3)
        elif instruction == "99":
            self.func_end()
        else:
            logging.debug("Error on finding function? %s" % instruction)
            logging.debug("A" + 1)
            
        if return_flag != None:
            return return_flag
            
            
            
            
            
            
    def process_program(self,input_vars):
        self.input_vars = input_vars
        self.position = 0
        logging.debug ("* Beginning program position %s *" % self.position)
        index = 0
        while self.position < len(self.data) and self.terminate is not True: 
            debug_1.append(self.data[:])
            pos_whole = str(self.data[self.position])
            pos = int(pos_whole[-1]) # last digit of instruction
#                logging.info("INDEX %s" % index)
            if pos_whole == "99":
                code = [self.data[self.position]]
                logging.info(">>>> Peforming code %s position %s relative_base %s" % (code,self.position,self.relative_base))
                self.perform_function(code)
                logging.debug("Finished on 99")
                self.position = len(self.data)
                self.terminate = True
                return self.output
            
            elif pos in [5,6]:
                code = self.data[self.position:self.position+3]
                logging.info(">>>> Peforming code %s position %s relative_base %s" % (code,self.position,self.relative_base))
                return_flag = self.perform_function(code)
                if return_flag != None:
                    self.position = return_flag
                else:
                    self.position += 3   
                            
            elif pos in [0,1,2,7,8]:
                code = self.data[self.position:self.position+4]
                logging.info(">>>> Peforming code %s position %s relative_base %s" % (code,self.position,self.relative_base))
                self.position += 4
                self.perform_function(code)
                
            elif pos in [3,9]:
                code = self.data[self.position:self.position+2]
                logging.info(">>>> Peforming code %s position %s relative_base %s" % (code,self.position,self.relative_base))
                self.position += 2
                self.perform_function(code)                    
        
            elif pos == 4:
                code = self.data[self.position:self.position+2]
                logging.info(">>>> Peforming code %s position %s relative_base %s" % (code,self.position,self.relative_base))
                self.position += 2
                self.perform_function(code)
                
            else:
                logging.info("Unknown opcode %s" % pos_whole)
                break
            index += 1
        return self.output
    
program = IntCode(data_input)
output = program.process_program([1])
logging.info("Output %s" % output)

program = IntCode(data_input)
output = program.process_program([2])
logging.info("Output %s" % output)