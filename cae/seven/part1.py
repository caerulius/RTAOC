import itertools
from subprocess import Popen, PIPE
import os
import sys

highest_signal = 0
for i in itertools.permutations([0,1,2,3,4]):
    current_signal = 0
    for j in i:
        p = Popen([sys.executable, 'computer.py'], stdin=PIPE, stdout=PIPE)
        p.stdin.write(bytes(str(j) + "\r\n", "utf-8"))
        p.stdin.write(bytes(str(current_signal) + "\r\n", "utf-8"))
        p.stdin.flush()
        out = p.stdout.readline()
        outInt = int(out.decode("utf-8").replace("\r", "").replace("\n", ""))
        current_signal = outInt
    if current_signal > highest_signal:
        highest_signal = current_signal

print(highest_signal)
