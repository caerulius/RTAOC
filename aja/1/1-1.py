import sys, math

with open(sys.argv[1],"r") as modules:
    total = 0
    for mass in modules:
        fuel = math.floor(int(mass) / 3) - 2
        total += fuel
    print(total)