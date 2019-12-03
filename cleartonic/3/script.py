import numpy as np

with open('input.txt','r') as f:
    data = f.readlines()
    wire1, wire2 = data[0].replace("\n",""), data[1].replace("\n","")
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")

board = np.zeros([20000,20000],dtype=int)

starting_x, starting_y = 10000, 10000
board[starting_x,starting_y] = 10 # arbitrary value set to 10 here


#################### 
# part 1
#################### 

    
def part_1():
        
    
   
    def check_presence(val, wire_num):
        # this says, if the wire is empty, just mark it with the current wire
        # also if the wire is crossing its own path, mark with current wire
        # but if it crosses a different wire, mark that as 3 
        
        if val == 0:
            return wire_num
        elif (val == 1 and wire_num == 1) or (val == 2 and wire_num == 2): 
            return wire_num
        elif (val == 1 and wire_num == 2) or (val == 2 and wire_num == 1): 
            return 3 # special cross case
        elif val == 3: # if its already crossed, leave it
            return 3
        elif val == 10: # starting point
            return 10
        else:
            print("Error on checking board presence?")
            return 7 
    
    def mark_path(current_x,current_y,instruction,wire_num):
        print("Wire %s instruction %s current_x %s current_y %s" % (wire_num,instruction,current_x,current_y))
        direction = instruction[0]
        steps = int(instruction[1:])
        # figure out direction first    
        # then mark all along the path, checking if a value is already there. remember 
        # to be checking that crossing its own wire does not count
        # later, we'll check wire 1 vs wire 2
        
        # ended up needing to set each board marking under its own direction conditional
        # range does not work with negative values 
        # so the x/y delta would have to come before
        
        # we have to deal with python's range starting at 0
        # so really we add 1 to all the endpoints so it marks
        # both the starting point and ending point
        # re-marking the starting point is fine
        # it's mostly the end point's proper position that matters
        # so we add or subtract 1 below to each range
        
        # example
        # 5000 current_x, 5000 current_y
        # instruction D120
        # endpoint_y = 120, endpoint_x = 0
        # mark all in range in both directions
        # x range is 5000 to 5000 (so, none)
        # y range is 5000 to 5120
        # then return new current position
        
        endpoint_x = current_x
        endpoint_y = current_y
    
        if direction == 'D':
            endpoint_y = current_y + steps
            for i in range(current_y, endpoint_y + 1):
                board[current_x,i] = check_presence(board[current_x,i], wire_num)
            
        elif direction == 'U':
            endpoint_y = current_y - steps
            for i in range(endpoint_y - 1, current_y):
                board[current_x,i] = check_presence(board[current_x,i], wire_num)
                
        elif direction == 'R':
            endpoint_x = current_x + steps
            for i in range(current_x, endpoint_x + 1):
                board[i,current_y] = check_presence(board[i,current_y], wire_num)
                
        elif direction == 'L':
            endpoint_x = current_x - steps
            for i in range(endpoint_x - 1,current_x):
                board[i,current_y] = check_presence(board[i,current_y], wire_num)
    
        # now update starting position and return
     
        return endpoint_x, endpoint_y # this becomes new starting position for next run 
        
        
        
            
    # first do wire1. we must isolate them
    # because crossing own wire is different
    current_x, current_y = starting_x, starting_y
    for instruction in wire1:
        current_x, current_y = mark_path(current_x, current_y, instruction, 1) # hardcode 1 for first wire num
    current_x, current_y = starting_x, starting_y
    for instruction in wire2:
        current_x, current_y = mark_path(current_x, current_y, instruction, 2) # hardcode 2 for second wire num
            
    global overlap_coords
    overlap_coords = [] # list of lists   
    for x in range(board.shape[0]):
        for y in range(board.shape[1]):
            if board[x,y] == 3:
                print("Overlap val 3 on coords %s %s" % (x,y))
                overlap_coords.append([x,y])
                
    # now find, among overlap_coords, min distance
    min_coords = []
    min_score = 10000000
    for coords in overlap_coords:
        x_dist = abs(coords[0]-starting_x)
        y_dist = abs(coords[1]-starting_y)
        score = x_dist + y_dist
        if score < min_score:
            min_coords = coords
            min_score = score
    print("Final coords %s min_distance %s" (min_coords,min_score))
                
























#################### 
# part 2
#################### 


# we'll make a dictionary per intersection
# and assign the number of steps each wire needs to reach
# we're going to have to store it as a string then parse later
def part_2():
    intersections = {}
    for i in overlap_coords:
        intersections[str(i)] = {'wire1':0,'wire2':0}
    
    #def part_2():
    def check_path(current_x,current_y,instruction,wire_num, current_steps):
        print("Wire %s instruction %s current_x %s current_y %s current_steps %s" % (wire_num,instruction,current_x,current_y, current_steps))
        direction = instruction[0]
        steps = int(instruction[1:])
        
        x_flag = False
        y_flag = False
        if direction == "D":
            endpoint_x = current_x
            endpoint_y = current_y + steps
            check_range = range(current_y, endpoint_y + 1)
            y_flag = True
        elif direction == "U":
            endpoint_x = current_x
            endpoint_y = current_y - steps
            check_range = range(endpoint_y - 1, current_y)
            y_flag = True
        elif direction == "R":
            endpoint_y = current_y
            endpoint_x = current_x + steps
            check_range = range(current_x, endpoint_x + 1)
            x_flag = True
        elif direction == "L":
            endpoint_y = current_y
            endpoint_x = current_x - steps
            check_range = range(endpoint_x - 1, current_x)
            x_flag = True
        # now read position of every step along the way, check if its a intersection
        
        for i in check_range:
            if x_flag:
                new_x_coord = i
                new_y_coord = current_y
            elif y_flag:
                new_x_coord = current_x
                new_y_coord = i
            
            
            # read current x/y
            cur_val = board[new_x_coord,new_y_coord]
    #        print("Current value %s at %s %s" % (cur_val,new_x_coord, new_y_coord))
    
            
            # if overlap
            if cur_val == 3:
                print("Intersection hit at %s %s" % (new_x_coord, new_y_coord))
                # find the matching intersection
    #            breakpoint()
                for inter in intersections:
                    x_coord = int(inter.split(", ")[0].replace("[",""))
                    y_coord = int(inter.split(", ")[1].replace("]",""))
                    if new_x_coord == x_coord and new_y_coord == y_coord:
                        print("Matching intersection found")
                        intersections[inter]['wire'+str(wire_num)] = current_steps
            if cur_val == 0:
                breakpoint()                    
            current_steps += 1
            
        # afterwards, remove 1 due to range issues above
        current_steps -= 1
            
            
        # mark new steps
        return endpoint_x, endpoint_y, current_steps # new starting position for next
    
    current_x, current_y = starting_x, starting_y
    current_steps = 0
    for instruction in wire1:
        current_x, current_y, current_steps = check_path(current_x, current_y, instruction, 1, current_steps) # hardcode 1 for first wire num
    current_x, current_y = starting_x, starting_y
    current_steps = 0
    for instruction in wire2:
        current_x, current_y, current_steps = check_path(current_x, current_y, instruction, 2, current_steps) # hardcode 2 for second wire num
    
    min_score = 10000000000
    min_intersection = ''
    for i in intersections:
        score = intersections[i]['wire1'] + intersections[i]['wire2']
        if score < min_score:
            min_score = score
            min_intersection = i
    print("Min intersection score %s " % min_score)