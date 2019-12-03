import numpy as np

# part 1
def part_1():
    with open('input.txt','r') as f:
        data = f.readlines()
        wire1, wire2 = data[0].replace("\n",""), data[1].replace("\n","")
        wire1 = wire1.split(",")
        wire2 = wire2.split(",")
        
    
    board = np.zeros([20000,20000],dtype=int)
    
    starting_x, starting_y = 10000, 10000
    board[starting_x,starting_y] = 10 # arbitrary value set to 10 here
    
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
                
