import re

file = open("input.txt", "r")
instructions = [instruction.rstrip('\n') for instruction in file]

# Part 1 

i=0
acc = 0
seen = []
while True:
    if(i >= len(instructions) or i in seen):
        break
    opp, arg = tuple(instructions[i].split(' '))
    seen.append(i)
    if(opp == 'acc'):
        acc += int(arg)
    elif(opp == 'jmp'):
        i += int(arg)
        continue
    i += 1

print(acc)

# Part 2 

class LoopException(Exception):
    """Base class for exceptions in this module."""
    pass


def run(line = 0, seen = [], swapped = False):
    acc = 0
    while True:
        if line == len(instructions): # If we got to the end of the file
            return acc

        if line in seen: # If already seen this line, we found a loop
            raise LoopException()

        opp, arg = tuple(instructions[line].split(' '))
        seen.append(line)

        if(opp == 'acc'):
            acc += int(arg)
            line += 1
            continue
        elif(opp == 'jmp'):
            # If we did not try to swap an instruction, we try it now by swapping 'jmp' by 'nop'.
            # If it fails, we continue as it is. Else we found the solution, we then return acc. 
            if not swapped:
                try:
                    return acc + run(line+1, seen.copy(), True)
                except LoopException:
                    pass
            line += int(arg)
            continue
        elif(opp == 'nop'):
            # If we did not try to swap an instruction, we try it now by swapping 'nop' by 'jmp'.
            # If it fails, we continue as it is. Else we found the solution, we then return acc. 
            if not swapped:
                try:
                    return acc + run(line+int(arg), seen.copy(), True)
                except LoopException:
                    pass
            line += 1
            continue

print(run())