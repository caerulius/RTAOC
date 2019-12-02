import math
data = '''148454
118001
98851
51106
113158
139801
126884
63241
71513
60490
131129
76176
74841
73589
130062
77999
140758
98182
101049
80951
75759
92666
142078
89196
124613
134713
75618
62680
141366
108899
88419
133385
90018
123521
51919
58191
109523
106012
94564
61103
72803
66309
143380
113708
146037
135176
131177
77109
108287
72170
87055
121407
126216
139520
120675
103833
130708
74029
149840
117122
105745
81186
51331
72686
52095
72612
76915
104859
114009
69714
130716
133106
73911
79766
56647
98035
103504
93728
111546
57637
68064
62803
72759
144845
80084
139247
139905
112807
87844
149388
76795
135703
120523
137422
108335
60206
133851
138574
141740
74398'''

#### PART 1
def get_fuel(x):
    temp = math.trunc(x/3)-2
    if temp <= 0:
        return 0
    else:
        return temp

def part_1():
    fuel_sum = 0
    for line in data.split("\n"):
        try:
            num = int(line)
            fuel_sum = fuel_sum + get_fuel(num)
        except Exception as e:
            print(e)
    print(fuel_sum)

#### PART 2
def part_2():
    fuel_sum = 0
    for line in data.split("\n"):
        try:
            num = int(line)
            module_fuel = 0
            last_fuel = get_fuel(num)
            # first add the latest to module
            module_fuel += last_fuel
            # then recursive until < 0 
            while last_fuel > 0:
                last_fuel = get_fuel(last_fuel)
                module_fuel += last_fuel
            fuel_sum += module_fuel 
            
        except Exception as e:
            print(e)
    print(fuel_sum)
    
    
