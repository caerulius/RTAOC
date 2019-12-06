class Node:
    def __init__(self, name, orbiting):
        self.name = name
        self.orbiting = orbiting

    def __str__(self):
        if self.orbiting is not None:
            return "{} is orbiting {}".format(self.name, self.orbiting.name)
        else:
            return "{} isn't orbiting anything".format(self.name)

    def getNumberOfOrbits(self):
        count = 0
        currOrbiting = self.orbiting
        while currOrbiting is not None:
            count = count + 1
            currOrbiting = currOrbiting.orbiting

        return count

    def getListOfOrbits(self):
        count = -1
        orbits = []
        currOrbiting = self.orbiting
        while currOrbiting is not None:
            count = count + 1
            orbits.append((currOrbiting, count))
            currOrbiting = currOrbiting.orbiting

        return orbits

class OrbitList:
    def __init__(self):
        self.bodies = []
        self.root = None

    def __str__(self):
        for i in self.bodies:
            print(i)

    def processOrbit(self, orbited, orbiting):
        orbitedNode = self.searchTree(orbited)
        orbitingNode = self.searchTree(orbiting)
        if orbitedNode is None:
            orbitedNode = Node(orbited, None)
            self.bodies.append(orbitedNode)

        if orbitingNode is None:
            orbitingNode = Node(orbiting, orbitedNode)
            self.bodies.append(orbitingNode)
        else:
            orbitingNode.orbiting = orbitedNode

    def searchTree(self, which):
        for i in self.bodies:
            if i.name == which:
                return i
        return None

    def getTotalOrbits(self):
        running = 0
        for i in self.bodies:
            running = running + i.getNumberOfOrbits()

        return running

OL = OrbitList()

with open("input.txt") as f:
    for line in f:
        data = line.replace("\n", "").split(")")

        OL.processOrbit(data[0], data[1])

YOUorbits = OL.searchTree("YOU").getListOfOrbits()
SANorbits = OL.searchTree("SAN").getListOfOrbits()

shortest = 99999
for i in YOUorbits:
    for j in SANorbits:
        if i[0] == j[0]:
            print("common orbit on {}, with YOUdist = {} and SANdist = {}".format(i[0].name, str(i[1]), str(j[1])))
            if i[1] + j[1] < shortest:
                shortest = i[1] + j[1]
                print("new shortest = {}".format(shortest))

print(shortest)
