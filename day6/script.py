import re

ANYONE=1
EVERYONE=2

file = open("input.txt", "r")
lines = [line.rstrip('\n') for line in file]

def countQuestions(lines, which):
    result = 0
    group = None
    for line in lines:

        if(len(line) == 0): # If its end of group
            result += len(group)
            group = None
            continue
            
        if(group == None): # If its first perso of group
            group = set(line)
            continue

        if(which == ANYONE):
            group = group.union(set(line))
        elif(which == EVERYONE): 
            group = group.intersection(set(line))

    result += len(group)
    return result

print(countQuestions(lines, ANYONE))
print(countQuestions(lines, EVERYONE))
