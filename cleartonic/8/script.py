import numpy as np
from matplotlib import pyplot as plt

with open('input.txt','r') as f:
    data = f.readlines()

data = data[0]
data = [int(i) for i in data]
num = 0
temp_layers = []
for i in range(int(len(data)/150)):
    temp_layers.append(data[num:num+150])
    num += 150
    
fewest_zero = []
min_zero = 500
for i in temp_layers:
    count = i.count(0)
    if count < min_zero:
        fewest_zero = i
        min_zero = count
        
print("Ones: %s Twos: %s Product %s" % (fewest_zero.count(1),fewest_zero.count(2),fewest_zero.count(1) * fewest_zero.count(2)))

layer2 = []
for layer in temp_layers:
    num = 0
    layer3 = []
    for i in range(6):
        layer3.append(layer[num:num + 25])
        num+=25
    layer2.append(layer3)
    
layers = [np.array(i) for i in layer2]

layer_indices = [i for i in range(0,100)]
y_coords = [i for i in range(0,6)]
x_coords = [i for i in range(0,24)]

final_image = np.zeros([6,25])
for x in x_coords:
    for y in y_coords:
        layer_index = 0
        while layers[layer_index][y][x] == 2:
            value = layers[layer_index][y][x]
            print("Layer %s x %s y %s value %s" % (layer_index,x,y,value))
            layer_index += 1
        value = layers[layer_index][y][x]
        print("Layer %s x %s y %s value %s" % (layer_index,x,y,value))
        
        # once loop breaks, that's the topmost non transparent value
        print("Placing value %s" % (value))
        final_image[y,x] = value

plt.imshow(final_image, interpolation='nearest')
plt.show()