with open('input.txt','r') as f:
    data = f.readlines()
data = [i.replace("\n","") for i in data if i != '']
        

class Map():
    def __init__(self,planets):
        self.planets = planets
    def find_planet(self,name):
        # take name, return planet
        try:
            return [i for i in self.planets if i.name == name][0]
        except:
            return None
    def add_planet(self,data):
        self.planets.append(Planet(data,normal_flag=False))
        
class Planet():
    def __init__(self,data):
        
        self.direct_orbits_count = 0
        self.indirect_orbits_count = 0
        self.data = data
        self.name = self.data.split(")")[1]
        self.direct_orbit = self.data.split(")")[0] # this is NOT that this Planet orbits X. It's that X planet orbits THIS
        

    def print(self):
        for k,v in self.__dict__.items():
            print("{:30}".format(str(k)),"{:10}".format(str(v)))
    
            
    
world_map = Map([Planet(i) for i in data])

def part_1():
    for index, starting_planet in enumerate(world_map.planets,1):
        num = 0        
        print("Index %s starting planet %s" % (index, starting_planet.name))
        
        # get first direct orbit planet
        direct_orbit = world_map.find_planet(starting_planet.direct_orbit)
    #    print("Current planet %s direct_orbit %s" % (starting_planet.name, direct_orbit.name))
        starting_planet.direct_orbits_count = 1
        
        while direct_orbit != None and direct_orbit.name != 'COM' and num < 10000:
            new_planet = world_map.find_planet(direct_orbit.direct_orbit)
    #        print("Current planet %s direct_orbit %s" % (direct_orbit.name, new_planet.name))
            direct_orbit = new_planet
            starting_planet.indirect_orbits_count += 1
            num +=1
        if num >= 10000:
            print("10k threshold error?")
            breakpoint()
    
    sum_orbits = 0
    for i in world_map.planets:
        sum_orbits += i.direct_orbits_count
        sum_orbits += i.indirect_orbits_count
    print("Total orbits %s " % sum_orbits)
    
def part_2():
    planet_YOU = world_map.find_planet("YOU")
    planet_SAN = world_map.find_planet("SAN")
    
    YOU_list = []
    next_planet = world_map.find_planet(planet_YOU.direct_orbit)
    YOU_list.append(next_planet.name)
    while next_planet is not None:
        next_planet = world_map.find_planet(next_planet.direct_orbit)
        if next_planet is not None:
            YOU_list.append(next_planet.name)
            
    SAN_list = []
    next_planet = world_map.find_planet(planet_SAN.direct_orbit)
    SAN_list.append(next_planet.name)
    while next_planet is not None:
        next_planet = world_map.find_planet(next_planet.direct_orbit)
        if next_planet is not None:
            SAN_list.append(next_planet.name)
            
    # find first instance in YOU where a common planet appears in order in SAN
    for i in YOU_list:
        if i in SAN_list:
            common_planet = i
            break
    
    # now find how long the list was for both up until common planet
    # this (them meeting at a common planet) is in essence the same as YOU traveling to SAN's orbit
    distance = YOU_list.index(common_planet) + SAN_list.index(common_planet)
    print("Distance from YOU to SAN %s" % distance)