data = range(136818,685979+1)
### part 1
def part_1():
    global valid_list
    valid_list = []
    for data_num in data:    
    #    print("Data num %s" % data_num)
        # check if increasing or equal order
        check1 = True
        for i in range(len(str(data_num))):
            try:
                if int(str(data_num)[i+1]) < int(str(data_num)[i]):
                    check1 = False
            except:
                pass
                
        if check1:
            # check if any adjacents (11, 22, etc)
            check2 = True
            if len(set([i for i in str(data_num)])) == len(str(data_num)):
                check2 = False
            
            if check2:
                valid_list.append(data_num)
            
    
    print(len(valid_list))
    
### part 2

def part_2():
    global valid_list2
    valid_list2 = []
    for data_num in valid_list:
        data_num_str = str(data_num)
        data_num_dict = {}
        for i in data_num_str:
            if i in data_num_dict:
                data_num_dict[i] = data_num_dict[i] + 1
            else:
                data_num_dict[i] = 1
        
        data_num_dict2 = {}
        for k, v in data_num_dict.items():
            if v > 1:
                data_num_dict2[int(k)] = v
        
        if 2 in data_num_dict2.values():
            valid_list2.append(data_num)
            
    print(len(valid_list2))
