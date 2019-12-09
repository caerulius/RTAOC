import itertools
from subprocess import Popen, PIPE
import os
import sys

highest_signal = 0

def translateOutput(output):
    print(output) #for some reason this line makes this work
    return int(output.decode("utf-8").replace("\r", "").replace("\n", ""))

def nextIndex(index):
    if index == 4:
        return 0
    return index+1

max_val = 0
for i in itertools.permutations(["5","6","7","8","9"]):
    amps = [Popen([sys.executable, 'computer.py'], stdin=PIPE, stdout=PIPE),
            Popen([sys.executable, 'computer.py'], stdin=PIPE, stdout=PIPE),
            Popen([sys.executable, 'computer.py'], stdin=PIPE, stdout=PIPE),
            Popen([sys.executable, 'computer.py'], stdin=PIPE, stdout=PIPE),
            Popen([sys.executable, 'computer.py'], stdin=PIPE, stdout=PIPE)]

    amps[0].stdin.write(bytes(i[0] + "\r\n", "utf-8"))
    amps[1].stdin.write(bytes(i[1] + "\r\n", "utf-8"))
    amps[2].stdin.write(bytes(i[2] + "\r\n", "utf-8"))
    amps[3].stdin.write(bytes(i[3] + "\r\n", "utf-8"))
    amps[4].stdin.write(bytes(i[4] + "\r\n", "utf-8"))

    index = 0
    amps[0].stdin.write(bytes("0\r\n", "utf-8"))
    amps[0].stdin.flush()

    while True:
        outInt = translateOutput(amps[index].stdout.readline())
        index = nextIndex(index)
        write = bytes(str(outInt) + "\r\n", "utf-8")
        amps[index].stdin.write(write)
        try:
            amps[index].stdin.flush()
        except:
            if outInt > max_val:
                max_val = outInt
            break

print(max_val)
