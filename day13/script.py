import re
import math

file = open("input.txt", "r")
notes = [data.rstrip('\n') for data in file]


timestamp = int(notes[0])
busIds = notes[1].split(',')

min = 1000
result = None
for i in range(len(busIds)):
    if busIds[i] == 'x':
        continue
    bus = int(busIds[i])
    diff = (math.floor(timestamp/bus)+1) * bus - timestamp
    if diff < min:
        min = diff
        result = bus

print("Part 1 result", result*min)


busIndices = dict()
for i in range(len(busIds)):
    if busIds[i] == 'x':
        continue
    busIndices[int(busIds[i])] = i
maxBus = max(busIndices.keys())

t = 100000000000000
found = False
while not found:
    found = True

    for bus in busIndices.keys():
        if (t+busIndices[bus]) % int(bus) != 0:
            found = False
            break

    if not found:
        # t += next(iter(busIndices.keys()))
        t += 303378947
    
    

    
        

print("Part 2 result", t)







